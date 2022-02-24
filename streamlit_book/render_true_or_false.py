import streamlit as st

try:
    from keywords import check_keyword
    from keywords import TRUE_FALSE_KEYWORD, BUTTON, SUCCESS, ERROR, DEFAULT_BUTTON_MESSAGE, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE
    from answers import save_answer
except:
    from .keywords import check_keyword
    from .keywords import TRUE_FALSE_KEYWORD, BUTTON, SUCCESS, ERROR, DEFAULT_BUTTON_MESSAGE, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE
    from .answers import save_answer


def true_or_false(question, answer, 
                    success=DEFAULT_SUCCESS_MESSAGE, 
                    error=DEFAULT_ERROR_MESSAGE, 
                    button=DEFAULT_BUTTON_MESSAGE):
    """Renders a true or false question from arguments.

    :param question: question to be displayed before the true or false options
    :type question: str
    :param answer: expected answer to the question, can be True or False
    :type answer: str
    :param success: message to be displayed when the user answers correctly. If empty, no message is displayed.
    :type success: str, optional
    :param error: message to be displayed when the user answers incorrectly. If empty, no message is displayed.
    :type error: str, optional
    :param button: message to be displayed on the button that checks the answer
    :type button: str, optional
    :return: tuple of booleans(button_pressed, answer_correct) with the button status and correctness of answer
    :rtype: tuple of bool
    """
    if len(question)==0:
        st.error("Please provide a question")
        return None, None
    else:
        key = question.lower().replace(" ","")
        user_answer = st.radio(question, options=["True", "False"], key=key)
        user_answer = (user_answer == "True") # Convert to boolean
        if st.button(button, key=key):
            # Reveal the answer
            if user_answer == answer:
                if success: 
                    st.success(success)
                is_correct = True
            else:
                if error: 
                    st.error(error)
                is_correct = False
            # Save the answer, if required
            if "save_answers" in st.session_state and st.session_state.save_answers:
                save_answer(question, is_correct=is_correct, user_answer=user_answer, correct_answer=answer)
            # Return if button is pressed and answer evaluation
            return True, is_correct
        else:
            # Not pressed yet
            return False, None

def true_or_false_parser(lines):
    """Parses a list of lines into a dictionary with the parsed values.

    :param lines: list of lines
    :type lines: list
    :return: parsed values for the true or false quizz type.
    :rtype: dict
    """

    # Dict to store the parsed values
    parse_dict = {}
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if check_keyword(line, TRUE_FALSE_KEYWORD):
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
    """Renders a true or false question from a list of lines.
    Used to parse from markdown.

    :param lines: list of lines
    :type lines: list
    :return: None
    """
    parse_dict = true_or_false_parser(lines)
    true_or_false(**parse_dict)
    return
