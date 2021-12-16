import streamlit as st

try:
    from keywords import check_keyword
    from keywords import MULTIPLE_CHOICE_KEYWORD, MULTIPLE_CHOICE_FALSE, MULTIPLE_CHOICE_TRUE
    from keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
except:
    from .keywords import check_keyword
    from .keywords import MULTIPLE_CHOICE_KEYWORD, MULTIPLE_CHOICE_FALSE, MULTIPLE_CHOICE_TRUE
    from .keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE

def multiple_choice_parser(lines):
    """Parses a list of lines into a dictionary with the parsed values.

    :param lines: list of lines
    :type lines: list
    :return: parsed values for the multiple choice quizz type.
    :rtype: dict
    """
    # Define default feedback messages 
    parse_dict = {
                    "question":"",
                    "options_dict":{},
                  }
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if check_keyword(line, MULTIPLE_CHOICE_KEYWORD):
                continue
        elif line.startswith(MULTIPLE_CHOICE_TRUE):
            option_text = line[len(MULTIPLE_CHOICE_TRUE):].strip()
            parse_dict["options_dict"][option_text] = True
        elif line.startswith(MULTIPLE_CHOICE_FALSE):
            option_text = line[len(MULTIPLE_CHOICE_FALSE):].strip()
            parse_dict["options_dict"][option_text] = False
        elif line.startswith(BUTTON):
            msg = line[len(BUTTON):].strip()
            parse_dict["button"] = msg  
        elif line.startswith(SUCCESS):
            msg = line[len(SUCCESS):].strip()
            parse_dict["success"] = msg  
        elif line.startswith(ERROR):
            msg = line[len(ERROR):].strip()
            parse_dict["error"] = msg
        else:
            # Put the rest of the lines into header as markdown
            parse_dict["question"] += line + "\n"
    return parse_dict


def multiple_choice(question, options_dict,  
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """Render a multiple choice question from the given parameters.

    :param question: question to be displayed before the multiple-choice options
    :type question: str
    :param options_dict: dictionary of options to be displayed, with the option text as key and the boolean answer as value
    :type options: dict
    :param answer: index (starting at 0) of the expected answer to the question
    :type answer: int
    :param success: message to be displayed when the user answers correctly
    :type success: str, optional
    :param error: message to be displayed when the user answers incorrectly
    :type error: str, optional
    :param button: message to be displayed on the button that checks the answer
    :type button: str, optional
    :return: boolean with the exit status of the function
    :rtype: bool
    """
    cb_list = []
    if len(question)==0:
        st.error("Please provide a question")
        return False
    elif len(options_dict)<2:
        st.error("Must have at least 2 options")
        return False
    else:
        # Write the question
        st.markdown(question)
        # Write the options and append the user answers into the list cb_list
        for option, answer in options_dict.items():
            key = (question + option + str(answer)).lower().replace(" ", "_")
            # Post the option with no option
            cb = st.checkbox(option, value=False, key=key)
            cb_list.append(cb)
        # Check if the correct checkboxes are checked
        key = ("multiple-choice:" + question + "".join(options_dict.keys())).lower().replace(" ", "_")
        if st.button(button, key=key):
            if all(u==a for u, a in zip(cb_list, options_dict.values())):
                st.success(success)
            else:
                st.error(error)
        return True

def multiple_choice_from_lines(lines):
    """Renders a multiple choice question from a list of lines.

    :param lines: list of lines
    :type lines: list
    :return: None
    """
    parse_dict = multiple_choice_parser(lines)
    multiple_choice(**parse_dict)
    return