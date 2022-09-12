import streamlit as st

try:
    from keywords import check_keyword
    from keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE, TODO_SUCCESS, SUCCESS
except:
    from .keywords import check_keyword
    from .keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE, TODO_SUCCESS, SUCCESS

def to_do_list(tasks, header="", success=TODO_SUCCESS):
    """ Renders the tasks as a to-do list, with optional header and success message.
    The tasks are a dictionary of tasks (supposed to be ordered as Python +3.6) 
    with their completed (True) or to-do (False) status as a checkbox.

    :param tasks: dictionary of tasks in format string:bool
    :type tasks: dict
    :param header: description of the tasks
    :type header: str, optional
    :param success: success message
    :type success: str, optional
    :return: boolean with the exit status of the function
    :rtype: bool   
    """
    if len(tasks)==0:
        st.error("There are no tasks to display.")
    cb_list = []
    st.markdown(header)
    for task, status in tasks.items():
        key = (header + task).lower().replace(" ", "_")
        cb = st.checkbox(task, value=status, key=key)
        cb_list.append(cb)
    if len(cb_list)>0 and all(cb for cb in cb_list):
        st.balloons()
        st.success(success)
        return True
    else:
        return False