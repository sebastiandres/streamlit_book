import streamlit as st

try:
    from keywords import *
except:
    from .keywords import *

def single_choice_parser(lines):
    """
    """
    # Define default feedback messages 
    parse_dict = {}
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(SINGLE_CHOICE_KEYWORD):
                continue
            else:
                raise st.error(f"Error in the format.")
        elif line.startswith(SINGLE_CHOICE_CORRECT):
            option_text = line[len(SINGLE_CHOICE_CORRECT):].strip()
            parse_dict["options"].append(option_text)
            if parse_dict["answer"] == "":
                parse_dict["answer"] = option_text
        elif line.startswith(SINGLE_CHOICE_WRONG):
            option_text = line[len(SINGLE_CHOICE_WRONG):].strip()
            parse_dict["options"].append(option_text)
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
            parse_dict["question"] += line
    return parse_dict

def single_choice_from_lines(lines):
    """
    Parse a single choice question from the given lines.
    """
    parse_dict = single_choice_parser(lines)
    return single_choice_from_lines(**parse_dict)

def single_choice(question, options, 
                    header="",
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """
    Render a single choice question from the given parameters.
    """
    st.markdown(header)
    if len(question)>0 and len(options)>0:
        user_answer = st.radio(question, options=options)
        if st.button(button):
            if user_answer == true_answer:
                st.success(success)
            else:
                st.error(error)
        return True
    else:
        return False