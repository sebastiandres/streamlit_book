
import streamlit as st
from glob import glob
import os
import pandas as pd

try:
    from .file_reader import get_all_files, create_buttons
    from .login import create_new_user_and_token, get_user_from_token, get_token_from_user  
    from .admin import admin_page
    from .helpers import get_git_revision_short_hash
    from .render import render_file
except Exception as e:
    print("Cannot import from . ", e)    
    from file_reader import get_all_files, create_buttons
    from login import create_new_user_and_token, get_user_from_token, get_token_from_user
    from admin import admin_page
    from helpers import get_git_revision_short_hash
    from render import render_file
except Exception as e:
    print("Cannot import! ", e)    

def get_query():
    """
    Depending on streamlit's version, uses the previous or the new way to get the query params.
    Previous: st.experimental_get_query_params()
    New: st.query_params()
    """
    if hasattr(st, "query_params"):
        return st.query_params.to_dict()
    else:
        return st.experimental_get_query_params()

def set_query_params(**kwargs):
    """
    Depending on streamlit's version, uses the previous or the new way to set the query params.
    Previous: st.experimental_set_query_params()
    New: st.set_query_params()
    """
    if hasattr(st, "query_params"):
        st.query_params.from_dict(**kwargs)
    else:
        st.experimental_set_query_params(**kwargs)

def set_chapter_config(
                        path="pages",
                        toc=False,
                        button="top",
                        button_previous="⬅️",
                        button_next="➡️",
                        button_refresh="🔄",
                        on_load_header=None,
                        on_load_footer=None,
                        save_answers=False,
                        display_page_info=True,
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
    :param save_answers: If True, it will save the answers in a csv file. Defaults to False.
    :type save_answers: bool
    :param display_page_info: If True, it will display the page info with the name and number. Defaults to True.
    :type display_page_info: bool
    :return: None
    """
    # Observation: File number goes from 0 to n-1.

    # Quick and dirty
    path = str(path)

    # Store the parameters
    if "save_answers" not in st.session_state:
        st.session_state.save_answers = save_answers
    if "commit_hash" not in st.session_state:
        st.session_state.commit_hash =  get_git_revision_short_hash()

    # Admin Login: if requested by the user on the url, it redirects to a specific amin page
    # Never shows the content, it will stay on the admin page.
    query_params = get_query_params()
    if "user" in query_params and "admin" in query_params["user"]:
        # Here we handle everything related to the admin
        admin_page()
        return # Don't show anything else!

    # User login
    if "user_id" not in st.session_state:
        query_params = get_query_params()
        if "token" in query_params:
            # Here we must handle the user session
            token = query_params["token"][0] #Just consider the first one
            ## If the token is wrong, notify the user.
            user_id = get_user_from_token(token)
            if user_id is None:
                # Wrong token
                st.error("Wrong token! Use the regular url.")
                return
            else:
                # Correct token
                st.session_state.user_id = user_id
                st.session_state.token = token
                # Redirect to avoid the url with the token
                del query_params["token"]
                st.experimental_set_query_params(**query_params)
        else:
            # Token not in query params: create a new user and token
            user_id, token = create_new_user_and_token()
            st.session_state.user_id = user_id
            st.session_state.token = token

    # Save answers behavior
    if st.session_state.save_answers:
        if "warned_about_save_answers" not in st.session_state:
            def on_click():
                st.session_state.warned_about_save_answers = True
            c1, c2 = st.columns([8,1])
            user_url = f"?token={st.session_state.token}"
            c1.warning(f"Your answers will be saved. You can relaunch the app using the following custom url (Save it!).\n\n{user_url}")
            c2.markdown("\n\n")
            c2.markdown("\n\n")
            c2.button("Dismiss", on_click=on_click)
            
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
                            display_page_info,
                            key="top")

        # Render the file using the magic
        try:
            render_file(selected_file_fullpath)
        except Exception as e:
            st.exception(e)

        # If required, put the button on the bottom of the page. Use columns for alignment
        if st.session_state.button in ["bottom", "both"]:
            create_buttons(caption_text, 
                            button_previous, button_next, button_refresh, 
                            display_page_info,
                            key="bottom")

        # Execute the on_load_footer function
        if on_load_footer:
            on_load_footer()
    return