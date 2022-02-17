#import streamlit.components.v1 as components
import streamlit as st
from glob import glob
#import os

try:
    from .render import render_file
except:
    from render import render_file

def on_toc_table_click():
    st.session_state.toc = False
    return

def on_previous_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.page_number = (st.session_state.page_number - 1) % st.session_state.total_files
    return

def on_next_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.page_number = (st.session_state.page_number + 1) % st.session_state.total_files
    return

def on_refresh_click():
    return

def create_buttons(caption_text, 
                    button_previous, 
                    button_next, 
                    button_refresh,
                    key=""):
    """
    Function to create the navigation buttons
    """
    st.caption(caption_text)
    p = len(button_previous)
    n = len(button_next)
    r = len(button_refresh)
    b = max(p,n,r)
    # Dinamic resizing based on length of the button names
    # Would be even better if layout type was known
    c1, c2, c3, c4 = st.columns([b, b, b, max(b, 20-3*b)])
    c1.button(button_previous, 
                help="Previous page", on_click=on_previous_click, key="previous_button_top"+key)
    c2.button(button_next, 
                help="Next page", on_click=on_next_click, key="next_button_top"+key)
    c3.button(button_refresh, 
                help="Refresh current page", on_click=on_refresh_click, key="switch_button_top"+key)
    return

def get_all_files(path):
    """
    Returns a list of all files (python, markdown) in the given path, 
    considering recursively all subfolders.
    It does not considers folders.
    Excludes files and folders starting with WIP (work in progress).
    It stores the total number of files (pages) in the session_state.
    """
    py_files = glob(f"{path}/**/*.py", recursive=True)
    md_files = glob(f"{path}/**/*.md", recursive=True)
    all_files = [_ for _ in sorted(py_files + md_files) if "/WIP" not in _]
    st.session_state.total_files = len(all_files)
    return all_files

def is_file(label):
    """
    Checks if the given label is a file.
    """
    return label.endswith(".py") or label.endswith(".md")

def get_options_at_path(user_selected_path: str, file_list: list):
    """
    Returns all the alternative items (folders and files) on the provided path
    """
    # Get the number of folders at the current level
    n_folders = len(user_selected_path.split("/"))
    # Get all the files at level
    subfolder_options = []
    for filepath in file_list:
        subfolder = "/".join(filepath.split("/")[:(n_folders+1)])
        if filepath.startswith(user_selected_path) and subfolder not in subfolder_options:
            subfolder_options.append(subfolder)
    options = [_.split("/")[-1] for _ in subfolder_options]
    return options

def get_selection_box_args_at_path(user_selected_path: str, file_list: list, level: int, selected_option: str=""):
    """
    Search for items: folders, python files or markdown files.
    Only looks for files at the given path.
    It returns a dictionary, with the required keys and values required by the selectbox
    """
    # Get all options at certain level
    options = get_options_at_path(user_selected_path, file_list)
    # Get the current label index
    if selected_option:
        index = options.index(selected_option)
    else:
        index = 0
    # Get all options at certain level
    selection_box_args = {
                        "label": f"Select {book_parts_convention(level)}:",
                        "options": options, 
                        "index": index,
                        "preset_option": options[index],                        
                        "key": f"select_box_{level}",
                        }
    return selection_box_args

def get_selection_boxes_args_from_filepath(file_fullpath: str, base_path: str, file_list: list):
    """
    Creates a list of dictionaries, with the required keys and values required by the selectbox.
    """
    # The relative path are only the folders in the filepath not on the base_path (but not the file itself)
    relative_path = file_fullpath.replace(f"{base_path}/", "")
    # Get the intermediate folders, but not the file itself
    selected_labels = relative_path.split("/")
    # Initialize and populate the list of dictionaries
    selection_boxes_args = []
    working_path = base_path
    for level, label in enumerate(selected_labels):
        # Get the options of the selectbox
        selection_box_args = get_selection_box_args_at_path(working_path, file_list, level, label)
        selection_boxes_args.append(selection_box_args)
        # Increate the path
        working_path = working_path + "/" + label
    return selection_boxes_args

def get_items(path: str):
    """
    # Search for folders, python files or markdown files.
    Only looks at precisely the level of the given path.
    It returns a dictionary, with keys the name to be rendered in the selectbox
    and with values another dictionary, with the type (file/folder) and the fullpath.
    """
    # Get all the files
    items_at_path = glob(f"{path}/*/") + glob(f"{path}/*.md") + glob(f"{path}/*.py")
    # Filter files that start with WIP (work in progress)
    items_at_path = [item for item in items_at_path if ("/WIP" not in item)]
    # Create
    item_dict = {}
    for i, my_item in enumerate(items_at_path):
        if my_item[-3:] in (".py", ".md"):
            item_name = my_item.split("/")[-1]
            render_name = item_name
            item_dict[render_name] = {"type":"file", "path":my_item}
        else:
            item_name = my_item.split("/")[-2]
            render_name = item_name
            item_dict[render_name] = {"type":"folder", "path":my_item}
    return item_dict

def set_book_config(path="pages",
                    toc=False,
                    button="top",
                    button_previous="⬅️",
                    button_next="➡️",
                    button_refresh="🔄",
                    on_load_header=None,
                    on_load_footer=None):
    """Sets the book configuration, and displays the selected file.

    :param path: The path to root directory of the the files (py or md) to be rendered as pages of the book. Can be a string (as in path="pages") or a dict with names for different books as in path={"book1":"pages_book1", "book2":"pages_book2"}.
    :type path: string, dict
    :param toc: If True, it will display the table of contents for the files on the path. Defaults to False.
    :type toc: bool
    :param button: "top" (default behavior) or "bottom".
    :type button: str
    :param button_previous: icon or text for the previous button.
    :type button_previous: str
    :param button_next: icon or text for the next button.
    :type button_next: str
    :param button_refresh: icon or text for the refresh button.
    :type button_refresh: str
    :param on_load_header: function to be called before the page is loaded.
    :type on_load_header: function
    :param on_load_footer: function to be called after the page is loaded.
    :type on_load_footer: function
    :return: None
    """
    # Observation: File number goes from 0 to n-1.
 
    # Get the files at path level (only files, not folders)
    file_list = get_all_files(path)

    # Check that we have at least 1 file to render
    if len(file_list) == 0:
        st.error(f"No files were found at the given path. Please check the provided path: {path}")
        return

    # Initialize the session state variables
    if "toc" not in st.session_state:
        st.session_state.toc = toc

    # Save button configuration
    if "button" not in st.session_state:
        st.session_state.button = button

    # Page number
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0

    # Update file_fullpath
    selected_file_fullpath = file_list[st.session_state.page_number]
    caption_text = f"Page {st.session_state.page_number+1} of {st.session_state.total_files}. File: {selected_file_fullpath}"

    if st.session_state.toc:
        option = st.radio("Table of contents", options=file_list)
        st.session_state.page_number = file_list.index(option)
        st.button("Go to page", on_click=on_toc_table_click, key="gotopage")
    else:
        # Execute the on_load_header function
        if on_load_header:
            on_load_header()

        # If required, put the button on top of the page. Use columns for alignment
        if st.session_state.button in ["top", "both"]:
            create_buttons(caption_text, 
                            button_previous, button_next, button_refresh,
                            key="top")

        # Render the file using the magic
        try:
            render_file(selected_file_fullpath)
        except Exception as e:
            st.exception(e)

        # If required, put the button on the bottom of the page. Use columns for alignment
        if st.session_state.button in ["bottom", "both"]:
            create_buttons(caption_text, button_previous, button_next, button_refresh, 
                            key="bottom")

        # Execute the on_load_footer function
        if on_load_footer:
            on_load_footer()
    return

def set_library_config(options, paths,
                        menu_title="Select a book",
                        menu_icon="book", 
                        icons=None, 
                        orientation=None, 
                        styles=None):
    """Creates a list of books using the streamlit_option_menu library.
    Renders the book based on the selection.
    Uses the same configurations used by streamlit-option-menu 
    (https://github.com/victoryhb/streamlit-option-menu)
    and icons from bootstrap icons (https://icons.getbootstrap.com/).

    :param options: List of book names to be displayed
    :type options: list of str
    :param paths: List of book paths containging the pages (py, md) to be displayed
    :type paths: list of str
    :param menu_title: Title of the menu, can be empty to be skipped.
    :type menu_title: str
    :param menu_icon: Icon to be used on the menu, from bootstrap icons.
    :type menu_icon: str
    :param icos: Icons to be used. Can be a single one used for all books, or a list of icons for each book.
    :type menu_icon: str or list of str
    :param orientation: Orientation of the menu. Can be "horizontal" or "vertical".
    :type orientation: str
    :param styles: Styles to be used. See the documentation of streamlit_option_menu.
    :type styles: dict
    """
    from streamlit_option_menu import option_menu

    # Initialize variables
    if "page_number" not in st.session_state:
        st.session_state.page_number = 0
    if "book_number" not in st.session_state:
        st.session_state.book_number = 0

    # Pack the arguments
    execution_dict = {"menu_title": menu_title, 
                      "options": options,
                      }
    args = [menu_icon, icons, orientation, styles]
    if menu_icon is not None: execution_dict["menu_icon"] = menu_icon
    if icons is not None: execution_dict["icons"] = icons
    if orientation is not None: execution_dict["orientation"] = orientation
    if styles is not None: execution_dict["styles"] = styles

    # Execute the menu
    if orientation=="horizontal":
        selected_book_name = option_menu(**execution_dict)
    else:
        with st.sidebar:
            selected_book_name = option_menu(**execution_dict)
    
    # Update variables
    selected_book_number = options.index(selected_book_name)
    if st.session_state.book_number != selected_book_number:
        st.session_state.book_number = selected_book_number
        st.session_state.page_number = 0
        
    # Launch the corresponding book
    set_book_config(path=paths[selected_book_number])
