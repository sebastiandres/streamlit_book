import streamlit as st

try:
    from keywords import *
    from render_to_do_list import to_do_list_from_lines
    from render_true_or_false import true_or_false_from_lines
    from render_multiple_choice import multiple_choice_from_lines
    from render_single_choice import single_choice_from_lines
    from render_text_input import text_input_from_lines
    from render_code_input import code_input_from_lines
    from render_file_upload import file_upload_from_lines
except:
    from .keywords import *
    from .render_to_do_list import to_do_list_from_lines
    from .render_true_or_false import true_or_false_from_lines
    from .render_multiple_choice import multiple_choice_from_lines
    from .render_single_choice import single_choice_from_lines
    from .render_text_input import text_input_from_lines
    from .render_code_input import code_input_from_lines
    from .render_file_upload import file_upload_from_lines

def render_file(fullpath):
    """
    Renders the file (it's always a file and not a folder)
    given the fullpath (path and filename).
    Only admits python or markdown, also by construction.
    """
    with open(fullpath) as fh:
        file_content = fh.read()
        if fullpath.endswith(".py"):
            exec(file_content)
        elif fullpath.endswith(".md"):
            chuncks = file_content.split("\n\n")
            clean_chuncks = [c.strip("\n") for c in chuncks]
            valid_chuncks = [c for c in clean_chuncks if len(c)>0]
            for chunck in valid_chuncks:
                print("chunk:", chunck)
                lines = chunck.split("\n")
                if lines[0].startswith(TODO_KEYWORD):
                    to_do_list_from_lines(lines)
                elif lines[0].startswith(TRUE_FALSE_KEYWORD):
                    true_or_false_from_lines(lines)
                elif lines[0].startswith(MULTIPLE_CHOICE_KEYWORD):
                    multiple_choice_from_lines(lines)
                elif lines[0].startswith(SINGLE_CHOICE_KEYWORD):
                    single_choice_from_lines(lines)
                elif lines[0].startswith(CODE_INPUT_KEYWORD):
                    code_input_from_lines(lines)
                elif lines[0].startswith(TEXT_INPUT_KEYWORD):
                    text_input_from_lines(lines)
                elif lines[0].startswith(FILE_UPLOAD_KEYWORD):
                    file_upload_from_lines(lines)
                else:
                    st.markdown("".join(lines), unsafe_allow_html=True)
        else:
            st.warning("File not supported")