import streamlit as st

try:
    from colored_expanders import add_color_to_expanders
except:
    from .colored_expanders import add_color_to_expanders

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
    elif fullpath_str.endswith(".md"):
        with open(fullpath, "r") as source_file:
            code = source_file.read()
            st.markdown(code)
            add_color_to_expanders()
    else:
        st.warning(f" ah: File extention not supported for file {fullpath}")
