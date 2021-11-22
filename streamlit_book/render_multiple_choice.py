import streamlit as st

try:
    from keywords import *
except:
    from .keywords import *


def multiple_choice_parser(lines):
    """
    """
    # Define default feedback messages 
    parse_dict = {}
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(MULTIPLE_CHOICE_KEYWORD):
                continue
        elif line.startswith(MULTIPLE_CHOICE_TRUE):
            option_text = line[len(MULTIPLE_CHOICE_TRUE):].strip()
            parse_dict["answers"][option_text] = True
        elif line.startswith(MULTIPLE_CHOICE_FALSE):
            option_text = line[len(MULTIPLE_CHOICE_FALSE):].strip()
            parse_dict["answers"][option_text] = False
        elif line.startswith(BUTTON):
            msg = line[len(BUTTON):].strip()
            parse_dict[BUTTON] = msg  
        elif line.startswith(SUCCESS):
            msg = line[len(SUCCESS):].strip()
            parse_dict[SUCCESS] = msg  
        elif line.startswith(ERROR):
            msg = line[len(ERROR):].strip()
            parse_dict[ERROR] = msg
        else:
            # Put the rest of the lines into header as markdown
            parse_dict["question"] += line + "\n"
    return parse_dict

def multiple_choice_from_lines(lines):
    """
    Parse a single choice question from the given lines.
    """
    parse_dict = multiple_choice_parser(lines)
    return multiple_choice_from_lines(**parse_dict)

def multiple_choice(question, options_dict,  
                    header="",
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """
    Render a single choice question from the given parameters.
    """
    st.markdown(header)
    cb_list = []
    st.markdown(question)
    for option, answer in options_dict.items():
        key = (question + option + answer).lower().replace(" ", "_")
        cb = st.checkbox(option, value=answer, key=key)
        cb_list.append(cb)
    if st.button(button):
        if all(u==a for u, a in zip(cb_list, parse_dict["options_dict"].values())):
            st.success(success)
        else:
            st.error(error)