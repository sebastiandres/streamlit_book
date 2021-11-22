import streamlit as st

try:
    from keywords import TRUE_FALSE_KEYWORD, BUTTON, SUCCESS, ERROR, DEFAULT_BUTTON_MESSAGE, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE
except:
    from .keywords import TRUE_FALSE_KEYWORD, BUTTON, SUCCESS, ERROR, DEFAULT_BUTTON_MESSAGE, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE


def true_or_false_parser(lines):
    """
    Parses the line into a dictionary of values of interest.
    """

    # Dict to store the parsed values
    parse_dict = {}
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(TRUE_FALSE_KEYWORD):
                continue
            else:
                break
        elif i==1:
            parse_dict["question"] = line
        elif i==2:
            answer = line.strip()
            if answer in ("True", "False"):
                parse_dict["answer"] = (answer == "True") # Convert to boolean, as required by the function
            else:
                break
        elif line.startswith(BUTTON):
            msg = line[len(BUTTON):].strip()
            parse_dict["button"] = msg  
        elif line.startswith(SUCCESS):
            msg = line[len(SUCCESS):].strip()
            parse_dict["success"] = msg  
        elif line.startswith(ERROR):
            msg = line[len(ERROR):].strip()
            parse_dict["error"] = msg
    return parse_dict

def true_or_false_from_lines(lines):
    """
    .
    """
    parse_dict = true_or_false_parser(lines)
    return true_or_false(**parse_dict)

def true_or_false(question, answer, 
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """
    Renders the question and the tasks as a to-do list.
    The tasks are a dictionary (supposed to be ordered as Python +3.6) of 
    tasks and their status as a checkbox.
    """
    if question:
        key = question.lower().replace(" ","")
        user_answer = st.radio(question, options=["True", "False"], key=key)
        user_answer = (user_answer == "True") # Convert to boolean
        if st.button(button):
            if user_answer == answer:
                st.success(success)
            else:
                st.error(error)
        return True
    else:
        return False 

if __name__=="__main__":
    question = "Is this a true or false statement?"
    answer = True
    # Raw question
    true_or_false(question, answer)
    # With all the options
    true_or_false(question+":", answer, success="Bien", error="Mal", button="Click")