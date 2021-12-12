import streamlit as st

try:
    from keywords import check_keyword
    from keywords import SINGLE_CHOICE_KEYWORD, SINGLE_CHOICE_CORRECT, SINGLE_CHOICE_WRONG
    from keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
except:
    from .keywords import check_keyword
    from .keywords import SINGLE_CHOICE_KEYWORD, SINGLE_CHOICE_CORRECT, SINGLE_CHOICE_WRONG, BUTTON, SUCCESS, ERROR
    from .keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE

def single_choice_parser(lines):
    """Parses a list of lines into a dictionary with the parsed values.

    :param lines: list of lines
    :type lines: list
    :return: parsed values for the single choice quizz type.
    :rtype: dict
    """
    # Define default feedback messages 
    parse_dict = {
                    "question":"",
                    "options":[],
                }
    answer = ""
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if check_keyword(line, SINGLE_CHOICE_KEYWORD):
                continue
            else:
                break
        elif line.startswith(SINGLE_CHOICE_CORRECT):
            option_text = line[len(SINGLE_CHOICE_CORRECT):].strip()
            parse_dict["options"].append(option_text)
            answer = option_text
        elif line.startswith(SINGLE_CHOICE_WRONG):
            option_text = line[len(SINGLE_CHOICE_WRONG):].strip()
            parse_dict["options"].append(option_text)
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
            parse_dict["question"] += line + "\n"
    # Store the answer_index
    parse_dict["answer_index"] = parse_dict["options"].index(answer)
    return parse_dict

def single_choice(question, options, answer_index,
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """Renders a single-choice question from arguments.

    :param question: question to be displayed before the single-choice options
    :type question: str
    :param options: list of options to be displayed.
    :type options: str
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
    if len(question)==0:
        st.error("Please provide a question")
        return False
    elif len(options)<2:
        st.error("Must have at least 2 options")
        return False
    else:
        # Write the options with radio button: only one option can be selected
        user_answer = st.radio(question, options=options)
        # Check if correct answer
        key = ("single-choice:" + question + "".join(options)).lower().replace(" ", "_")
        if st.button(button, key=key):
            if options.index(user_answer) == answer_index:
                st.success(success)
            else:
                st.error(error)
        return True


def single_choice_from_lines(lines):
    """Renders a single choice question from a list of lines.

    :param lines: list of lines
    :type lines: list
    :return: None
    """
    parse_dict = single_choice_parser(lines)
    single_choice(**parse_dict)
    return
