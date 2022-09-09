import streamlit as st
from glob import glob
import os
import pandas as pd

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
                    display_page_info,
                    key=""):
    """
    Function to create the navigation buttons.
    Only applies if more than 1 file is to be rendered.
    """
    # Skip if there is only one file
    if st.session_state.total_files <= 1:
        return
    # We have at least 2 files, so render the buttons
    if display_page_info:
        st.caption(caption_text)
    p = len(button_previous)
    n = len(button_next)
    r = len(button_refresh)
    b = max(p,n,r)
    # Dinamic resizing based on length of the button names
    # Would be even better if layout type was known
    c1, c2, c3, c4 = st.columns([b, b, b, max(b, 20-3*b)])
    if st.session_state.page_number!=0:
        c1.button(button_previous, 
                    help="Previous page", on_click=on_previous_click, key="previous_button_top"+key)
    if st.session_state.page_number!=st.session_state.total_files-1:
        c2.button(button_next, 
                    help="Next page", on_click=on_next_click, key="next_button_top"+key)
    c3.button(button_refresh, 
            help="Refresh current page", on_click=on_refresh_click, key="switch_button_top"+key)
    return

def get_all_files(path):
    """
    Returns a list of all files (python, markdown) in the given path, 
    considering recursively all subfolders.
    The path can be a single file.
    It does not considers folders.
    Excludes files and folders starting with WIP (work in progress).
    It stores the total number of files (pages) in the session_state.
    """
    if path.endswith(".py"):
        py_files = [ path, ]
    else:
        py_files = glob(f"{path}/**/*.py", recursive=True)
    if path.endswith(".md"):
        md_files = [ path, ]
    else:
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
