import streamlit.components.v1 as components
import streamlit as st
from glob import glob
import os

try:
    from .render import render_file
except:
    from render import render_file

def update_page():
    """
    Updates the url with the queries for the page based on the file_number.
    If the book_catalog has more than one book, includes the book name on the query parameters.
    """   
    query_params = {"page": st.session_state.file_number}
    if len(st.session_state.path_dict) >= 2:
        query_params["book"] = st.session_state.active_book
    st.experimental_set_query_params(**query_params)
    return

def on_gotopage_click():
    st.session_state.toc = False
    return

def on_refresh_click():
    return

def on_next_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number + 1) % st.session_state.total_files
    update_page()
    return

def on_previous_click():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number - 1) % st.session_state.total_files
    update_page()
    return

def create_buttons(caption_text, 
                    button_previous, 
                    button_next, 
                    button_refresh,
                    username, repository, key=""):
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
    if len(username+repository) > 0:
        c4.markdown(f"[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FP{username}%2F{repository}&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)",
                    unsafe_allow_html=True)
    return

def get_all_files():
    """
    Returns a list of all files (python, markdown) in the given path, 
    considering recursively all subfolders.
    It does not considers folders.
    Excludes files and folders starting with WIP (work in progress).
    It stores the total number of files (pages) in the session_state.
    """
    active_book = st.session_state.active_book
    path = st.session_state.path_dict[active_book]
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
                    on_load_footer=None,
                    username="",
                    repository=""):
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
    :param username: GitHub username (for the hits counter).
    :type username: str
    :param repository: GitHub repository (for the hits counter).
    :type repository: str
    :return: None
    """
    # Observation: File number goes from 0 to n-1.
 
    # Process the path, depending on the type
    ## For a string
    if type(path) is str:
        # Convert to dict of 1 book
        path = {book: path}
    ## For a dict
    if type(path) is dict:
        # Process the path for each book
        clean_path = {}
        for book_name, book_path in path.items():
            clean_book_name = book_name.replace(" ", "_")
            clean_book_path = book_path
        st.session_state.path_dict = path
    else:
        raise ValueError("The path must be a string or a dict.")
        return

    # Define current active book:
    # Get the query parameters (if any)
    query_params = st.experimental_get_query_params()
    # If a valid book is provided by the query, use it. Otherwise, use the first defined one.
    first_book = list(st.session_state.path_dict.keys())[0]
    if "book" in query_params:     
        query_book = query_params["book"][0] # The first book, always a list.
        if query_book in st.session_state.path_dict.keys():
            st.session_state.active_book = query_book
        else:
            st.error("The book you selected does not exist. Redirecting to first valid book")
            st.session_state.active_book = first_book
    else:
        if "active_book" not in st.session_state:
            st.session_state.active_book = first_book

    # Get the files at path level (only files, not folders)
    file_list = get_all_files()

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
    query_parameters = st.experimental_get_query_params()
    if "page" in query_parameters:
        page = int(query_parameters["page"][0]) # Get the first of all provided values
        page_in_range = min(max(page, 0), len(file_list)-1)
        if page_in_range != page:
            st.error(f"The page number {page} is out of range. Redirected to initial page.")
            st.session_state.file_number = page_in_range
            update_page()
        else:
            st.session_state.file_number = page_in_range
    else:
        # if page not in query params, send to the correct page
        st.session_state.file_number = 0
        update_page()

    # Update file_fullpath
    selected_file_fullpath = file_list[st.session_state.file_number]
    caption_text = f"Page {st.session_state.file_number+1} of {st.session_state.total_files}. File: {selected_file_fullpath}"

    if st.session_state.toc:
        option = st.radio("Table of contents", options=file_list)
        st.session_state.file_number = file_list.index(option)
        st.button("Go to page", on_click=on_gotopage_click, key="gotopage")
    else:
        # Execute the on_load_header function
        if on_load_header:
            on_load_header()

        # If required, put the button on top of the page. Use columns for alignment
        if st.session_state.button in ["top", "both"]:
            create_buttons(caption_text, 
                            button_previous, button_next, button_refresh,
                            username, repository, key="top")

        # Render the file using the magic
        try:
            render_file(selected_file_fullpath)
        except Exception as e:
            st.exception(e)

        # If required, put the button on the bottom of the page. Use columns for alignment
        if st.session_state.button in ["bottom", "both"]:
            create_buttons(caption_text, button_previous, button_next, button_refresh, 
                            username, repository, key="bottom")

        # Execute the on_load_footer function
        if on_load_footer:
            on_load_footer()
    return