import streamlit as st

try:
    from keywords import check_keyword
    from keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE, TODO_SUCCESS, SUCCESS
except:
    from .keywords import check_keyword
    from .keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE, TODO_SUCCESS, SUCCESS

def to_do_list_parser(lines):
    """Parses a list of lines into a dictionary with the parsed values.

    :param lines: list of lines
    :type lines: list
    :return: parsed values for tasks, and optionally the header and success message.
    :rtype: dict
    """
    # Dict to store the parsed values
    parse_dict = {
                    "tasks":{},
                    "header":"",
                    "success":TODO_SUCCESS,
                }
    for i, line in enumerate(lines):
        if i==0:
            if check_keyword(line, TODO_KEYWORD):
                continue
            else:
                break
        elif line.startswith(TODO_COMPLETED):
            task = line[len(TODO_COMPLETED):].strip()
            parse_dict["tasks"][task] = True
        elif line.startswith(TODO_INCOMPLETE):
            task = line[len(TODO_INCOMPLETE):].strip()
            parse_dict["tasks"][task] = False
        elif line.startswith(SUCCESS):
            parse_dict["success"] = line[len(SUCCESS):].strip()
        else:
            parse_dict["header"] += line
    return parse_dict


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

def to_do_list_from_lines(lines):
    """Renders a to-do list from a list of lines.

    :param lines: list of lines
    :type lines: list
    :return: None
    """
    parse_dict = to_do_list_parser(lines)
    to_do_list(tasks=parse_dict["tasks"], 
                header=parse_dict["header"], 
                success=parse_dict["success"])
    return