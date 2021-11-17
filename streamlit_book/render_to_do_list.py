import streamlit as st

from .keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE

def render_to_do_list(lines):
    """
    """
    true_solution_dict = {}
    cb_list = []
    for i, line in enumerate(lines):
        if line.startswith(TODO_KEYWORD):
            continue
        elif line.startswith(TODO_COMPLETED):
            activity = line[len(TODO_COMPLETED):].strip()
            cb = st.checkbox(activity, value=True)
            cb_list.append(cb)
            true_solution_dict[activity] = True
        elif line.startswith(TODO_INCOMPLETE):
            activity = line[len(TODO_INCOMPLETE):].strip()
            cb = st.checkbox(activity, value=False)
            cb_list.append(cb)
            true_solution_dict[activity] = False
        else:
            st.markdown(line)
    if len(cb_list)>0 and all(cb for cb in cb_list):
        st.balloons()
        st.success('All done!')
    return true_solution_dict
