import streamlit as st
from glob import glob
import os

try:
    from .render import render_file
except:
    from render import render_file

def on_switch_click():
    """
    Alternates between one navigation method (button or selectbox)
    """
    st.session_state.navigate_with_buttons = not st.session_state.navigate_with_buttons
    return

def on_bookmark_click():
    """
    Stores current page as the initial page
    """
    with open("bookmark.txt", "w") as f:
        f.write(str(st.session_state.file_number))
    return

def on_next_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number + 1) % st.session_state.total_files
    return

def on_previous_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number - 1) % st.session_state.total_files
    return

def book_parts_convention(level):
    """
    Returns the name of the chapter/section at the given level.
    """
    book_convention_dict = {0:"section", 1:"chapter", 2:"subchapter", 3:"content"}
    return book_convention_dict[min(level, len(book_convention_dict))]

def get_all_files(path: str):
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

def set_book_config(path: str, 
                    button: str="bottom", 
                    button_next: str="➡️",
                    button_previous: str="⬅️",
                    button_bookmark="🔖",
                    button_switch_method="🔄"):
    """
    Renders a dynamically filled sidebar with selectboxes, allowing
    the user to select a file that gets displayed on the main view.
    It uses recursion to navigate though the folder selections until
    reaching a file that can be render.
    """
    # Parameters: File number goes from 0 to n-1.
    # Look for bookmark file in the folder
    if os.path.isfile(f"bookmark.txt"):
        with open("bookmark.txt", "r") as f:
            INITIAL_FILE_NUMBER = int(f.read())
    else:
        INITIAL_FILE_NUMBER = 0
    # Sanitize the path
    if path.endswith("/"):
        path = path[:-1]
    # Initialize the session state variables
    if "file_number" not in st.session_state:
        st.session_state.file_number = INITIAL_FILE_NUMBER
    if "navigate_with_buttons" not in st.session_state:
        valid_button_argument = button in ("top", "bottom")
        st.session_state.navigate_with_buttons = valid_button_argument
    # Get the files at path level (only files, not folders)
    file_list = get_all_files(path)
    # Check that we have at least 1 file to render
    if len(file_list) == 0:
        st.error(f"No files were found at the given path. Please check the provided path: {path}")
        return

    c1, c2, c3, c4, c5 = st.columns([0.9, 0.1, 0.1, 0.1, 0.1])
    if button_bookmark:
        c4.button(button_bookmark, on_click=on_bookmark_click, key="bookmark_button_top")
    if button_switch_method:
        c5.button(button_switch_method, on_click=on_switch_click, key="switch_button_top")

    if st.session_state.navigate_with_buttons:
        # Update file_fullpath
        selected_file_fullpath = file_list[st.session_state.file_number]
        # If required, put the button on top of the page. Use columns for alignment
        c1.caption(f"Page {st.session_state.file_number+1} of {st.session_state.total_files}. File: {selected_file_fullpath}")
        if button=="top":
            c2.button(button_previous, on_click=on_previous_click, key="previous_button_top")
            c3.button(button_next, on_click=on_next_click, key="next_button_top")
        # Render the file using the magic
        render_file(selected_file_fullpath)
        # If required, put the button on the bottom of the page. Use columns for alignment
        if button=="bottom":
            c2.button(button_previous, on_click=on_previous_click, key="previous_button_bottom")
            c3.button(button_next, on_click=on_next_click, key="next_button_bottom")
        ## Autor
        st.caption("Streamlit book - created by [sebastiandres](https://sebastiandres.xyz) - Nov 2021")    
    else:
        # If no button, use the lateral sidebar to navigate
        # Depth counter, naming convention for content (depending on depth), 
        # and a wrapper function to call it more easily
        depth = 1
        book_convention_dict = {1:"section", 2:"chapter", 3:"subchapter", 4:"content"}
        book_naming = lambda n: book_convention_dict[min(n, len(book_convention_dict))]
        # Get the items (files/folders) at path level
        items_at_path_dict = get_items(path=path)
        # Provide a select box for user to select, if not an empty list:
        if len(items_at_path_dict)>0:
            selected_item = st.sidebar.selectbox(f"Select {book_naming(depth)}:", 
                                                options=sorted(items_at_path_dict.keys()),
                                                key=f"select_box_{depth}")
            item_dict = items_at_path_dict[selected_item]
            # Depending on selection, render if file or procede recursively
            while item_dict["type"]!="file" or len(items_at_path_dict)==0:
                depth += 1
                items_at_path_dict = get_items(item_dict["path"])
                # Provide the select box for current items
                if len(items_at_path_dict)>0:
                    selected_item = st.sidebar.selectbox(f"Select {book_naming(depth)}:", 
                                                        options=sorted(items_at_path_dict.keys()),
                                                        key=f"select_box_{depth}")
                    item_dict = items_at_path_dict[selected_item]
                else:
                    break
            # Render the file, if we got one!
            if item_dict["type"]=="file":
                st.caption(item_dict["path"])
                render_file(fullpath=item_dict["path"])
            else:
                st.warning("Empty folder")
        ## Autor
        st.sidebar.caption("[Streamlit book](https://streamlit_book.readthedocs.io/) - [sebastiandres](https://sebastiandres.xyz) - Nov 2021")
    return