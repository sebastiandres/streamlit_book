import sys
import types

import streamlit as st

try:
    from colored_expanders import add_color_to_expanders
except:
    from .colored_expanders import add_color_to_expanders


def _new_module(name: str) -> types.ModuleType:
    """Create a new module with the given name."""
    return types.ModuleType(name)


def render_file(fullpath):
    """
    Renders the file (it's always a file and not a folder)
    given the fullpath (path and filename).
    Only admits python or markdown, also by construction.
    """
    fullpath_str = str(fullpath)
    if fullpath_str.endswith(".py"):
        # Create fake module. This gives us a name global namespace to
        # execute the code in.
        module = _new_module("__main__")

        # Install the fake module as the __main__ module. This allows
        # the pickle module to work inside the user's code, since it now
        # can know the module where the pickled objects stem from.
        # IMPORTANT: This means we can't use "if __name__ == '__main__'" in
        # our code, as it will point to the wrong module!!!
        sys.modules["__main__"] = module

        # Add special variables to the module's globals dict.
        # Note: The following is a requirement for the CodeHasher to
        # work correctly. The CodeHasher is scoped to
        # files contained in the directory of __main__.__file__, which we
        # assume is the main script directory.
        module.__dict__["__file__"] = fullpath

        # Execute as a regular python file
        with open(fullpath, "rb") as source_file:
            code = compile(source_file.read(), fullpath, "exec")
        exec(code, module.__dict__)

        add_color_to_expanders()
    elif fullpath_str.endswith(".md"):
        with open(fullpath, "r") as source_file:
            code = source_file.read()
            st.markdown(code)
            add_color_to_expanders()
    else:
        st.warning(f" ah: File extention not supported for file {fullpath}")
