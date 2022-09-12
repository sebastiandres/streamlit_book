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
        user_answer_str = st.radio(question, options=["True", "False"], key="TF"+key)
        user_answer = (user_answer_str == "True") # Convert to boolean
        if st.button(button, key="button"+key):
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