
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
    from .chapter_config import set_chapter_config
except Exception as e:
    print("Cannot import from . ", e)    
    from file_reader import get_all_files, create_buttons
    from login import create_new_user_and_token, get_user_from_token, get_token_from_user
    from admin import admin_page
    from helpers import get_git_revision_short_hash
    from render import render_file
    from chapter_config import set_chapter_config
except Exception as e:
    print("Cannot import! ", e)    

def set_book_config(options, paths,
                        menu_title="Select a chapter",
                        menu_icon="book", 
                        icons=None, 
                        orientation=None, 
                        styles=None,
                        save_answers=False,
                        display_page_info=True,
                        ):
    """Creates a book using the streamlit_option_menu library.
    Renders each of the corresponding chapters based on their properties.
    Uses the same configurations used by `streamlit-option-menu 
    <https://github.com/victoryhb/streamlit-option-menu>`_
    and icons from `bootstrap-icons <https://icons.getbootstrap.com/>`_.

    :param options: List of chapter names to be displayed
    :type options: list of str
    :param paths: List of chapter paths containging the pages (py, md) to be displayed
    :type paths: list of str
    :param menu_title: Title of the menu, can be empty to be skipped.
    :type menu_title: str
    :param menu_icon: Icon to be used on the menu, from bootstrap icons.
    :type menu_icon: str
    :param icons: Icons to be used. Can be a single one used for all books, or a list of icons for each book.
    :type menu_icon: str or list of str
    :param orientation: Orientation of the menu. Can be "horizontal" or "vertical".
    :type orientation: str
    :param styles: Styles to be used. See the documentation of streamlit_option_menu.
    :type styles: dict
    :param save_answers: If True, it will save the answers in a csv file. Defaults to False.
    :type save_answers: bool
    :param display_page_info: If True, it will display the page info with the name and number. Defaults to True.
    :type display_page_info: bool
    :return: None
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
        
    # Launch the corresponding chapter
    set_chapter_config(path=paths[selected_book_number], save_answers=save_answers, display_page_info=display_page_info)
