import streamlit as st

try:
    #from keywords import *
    from colored_expanders import add_color_to_expanders
    #from render_to_do_list import to_do_list_from_lines
    #from render_true_or_false import true_or_false_from_lines
    #from render_multiple_choice import multiple_choice_from_lines
    #from render_single_choice import single_choice_from_lines
    #from render_text_input import text_input_from_lines
    #from render_code_input import code_input_from_lines
    #from render_file_upload import file_upload_from_lines
    #from social_media import share_from_lines
except:
    #from .keywords import *
    from .colored_expanders import add_color_to_expanders
    #from .render_to_do_list import to_do_list_from_lines
    #from .render_true_or_false import true_or_false_from_lines
    #from .render_multiple_choice import multiple_choice_from_lines
    #from .render_single_choice import single_choice_from_lines
    #from .render_text_input import text_input_from_lines
    #from .render_code_input import code_input_from_lines
    #from .render_file_upload import file_upload_from_lines
    #from .social_media import share_from_lines

def render_file(fullpath):
    """
    Renders the file (it's always a file and not a folder)
    given the fullpath (path and filename).
    Only admits python or markdown, also by construction.
    """
    fullpath_str = str(fullpath)
    if fullpath_str.endswith(".py"):
        # Execute as a regular python file 
        with open(fullpath, "rb") as source_file:
            code = compile(source_file.read(), fullpath, "exec")
        exec(code, globals(), locals())
        add_color_to_expanders()
    else:
        st.warning(f"File extention not supported for file {fullpath}")