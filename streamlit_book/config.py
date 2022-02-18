
import streamlit as st
from glob import glob
import os
import pandas as pd

from .render import render_file
try:
    from .file_reader import * # change later
    from .login import *
    from .answers import get_git_revision_short_hash
except:
    #from render import render_file
    from file_reader import * # change later
    from login import *
    from answers import get_git_revision_short_hash

def set_book_config(path="pages",
                    toc=False,
                    button="top",
                    button_previous="⬅️",
                    button_next="➡️",
                    button_refresh="🔄",
                    on_load_header=None,
                    on_load_footer=None,
                    user_login=False,
                    save_answers=False,
                    ):
    """Sets the book configuration, and displays the selected file.

    :param path: The path to root directory of the the files (py or md) to be rendered as pages of the book. 
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

    # Save login and answers behavior
    if "user_login" not in st.session_state:
        st.session_state.user_login = user_login
    if "save_answers" not in st.session_state:
        st.session_state.save_answers = save_answers

    # Admin Login: if requested by the user on the url, it redirects to a specific amin page
    # Never shows the content, it will stay on the admin page.
    query_params = st.experimental_get_query_params()
    if "user" in query_params and "admin" in query_params["user"]:
        admin_page()
        return

    # User login, if requested
    if user_login and ("password_correct" not in st.session_state or not st.session_state["password_correct"]):
        user_login_page()
        return


    # Get commit_hash
    if "commit_hash" not in st.session_state:
        st.session_state.commit_hash =  get_git_revision_short_hash()

    # Get user_id
    if "user_id" not in st.session_state:
        st.session_state.user_id = get_current_user_id()
    #st.experimental_show(st.session_state.user_id)

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
    execution_dict = {
                        "menu_title": menu_title, 
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
