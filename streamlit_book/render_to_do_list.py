import streamlit as st

def parse_to_do_list(lines):
    """
    Parses the line into a dictionary of values of interest.
    """
    from .keywords import TODO_KEYWORD, TODO_COMPLETED, TODO_INCOMPLETE, ERROR
    # Dict to store the parsed values
    parse_dict = {
                    "tasks":{}, 
                    "header":""
                }
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(TODO_KEYWORD):
                continue
            else:
                return {ERROR: "There is an error in the format"}
        elif line.startswith(TODO_COMPLETED):
            task = line[len(TODO_COMPLETED):].strip()
            parse_dict["tasks"][task] = True
        elif line.startswith(TODO_INCOMPLETE):
            task = line[len(TODO_INCOMPLETE):].strip()
            parse_dict["tasks"][task] = False
        else:
            parse_dict["header"] = line
    return parse_dict

def to_do_list(tasks, header=""):
    """
    Renders the optional header and the tasks as a to-do list.
    The tasks are a dictionary (supposed to be ordered as Python +3.6) of 
    tasks and their status as a checkbox.
    """
    cb_list = []
    st.markdown(header)
    for task, status in tasks.items():
        key = (header + task).lower().replace(" ", "_")
        cb = st.checkbox(task, value=status, key=key)
        cb_list.append(cb)
    if len(cb_list)>0 and all(cb for cb in cb_list):
        st.balloons()
        st.success('All done!')
        return True
    else:
        return False

def to_do_list_from_lines(lines):
    """
    Renders a to-do list from a list of lines.
    """
    parse_dict = parse_to_do_list(lines)
    to_do_list(tasks=parse_dict["tasks"], header=parse_dict["header"])
    return

if __name__=="__main__":
    render_to_do_list({"a":True, "b":False, "c":True}, header="To do list")
