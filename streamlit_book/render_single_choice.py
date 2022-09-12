import streamlit as st

try:
    from keywords import check_keyword
    from keywords import SINGLE_CHOICE_KEYWORD, SINGLE_CHOICE_CORRECT, SINGLE_CHOICE_WRONG
    from keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
    from answers import save_answer
except:
    from .keywords import check_keyword
    from .keywords import SINGLE_CHOICE_KEYWORD, SINGLE_CHOICE_CORRECT, SINGLE_CHOICE_WRONG, BUTTON, SUCCESS, ERROR
    from .keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
    from .answers import save_answer


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
    :return: tuple of booleans with button press status and correctness of answer
    :rtype: tuple of bool 
    """
    if len(question)==0:
        st.error("Please provide a question")
        return None, None
    elif len(options)<2:
        st.error("Must have at least 2 options")
        return None, None
    else:
        # Write the options with radio button: only one option can be selected
        user_answer = st.radio(question, options=options)
        # Check if correct answer
        key = ("single-choice:" + question + "".join(options)).lower().replace(" ", "_")
        if st.button(button, key=key):
            # Check ansers
            if options.index(user_answer) == answer_index:
                if success:
                    st.success(success)
                is_correct = True
            else:
                if error:
                    st.error(error)
                is_correct = False
            # Save the answers, if required
            if "save_answers" in st.session_state and st.session_state.save_answers:
                save_answer(question, is_correct=is_correct, user_answer=user_answer, correct_answer=options[answer_index])
            # Return if button is pressed and answer evaluation
            return True, is_correct
        else:
            # Return if button is not pressed
            return False, None
