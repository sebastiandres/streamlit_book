import streamlit as st

try:
    from keywords import *
    from answers import save_answer
except:
    from .keywords import *
    from .answers import save_answer

def code_input(question, initial_code,
                contains=[],
                equals="",
                normalization_function=None,
                verification_function=None,
                success=DEFAULT_SUCCESS_MESSAGE, 
                error=DEFAULT_ERROR_MESSAGE, 
                button=DEFAULT_BUTTON_MESSAGE):
    """Render a text input question from the given parameters.

    :param question: question to be displayed before the multiple-choice options
    :type question: str
    :param initial_code: 
    :type initial_code: str
    :param contains: 
    :type contains: list of str
    :param equals: 
    :type equals: str
    :param normalization_function: 
    :type normalization_function: function
    :param verification_function: 
    :type verification_function: function
    :param success: message to be displayed when the user answers correctly
    :type success: str, optional
    :param error: message to be displayed when the user answers incorrectly
    :type error: str, optional
    :param button: message to be displayed on the button that checks the answer
    :type button: str, optional
    :return: tuple of booleans with button press status and correctness of answer
    :rtype: tuple of bool
    """
    user_code = st.text_input(question, initial_code)
    # Check if the correct checkboxes are checked
    key = ("text-input:" + question + "/" + initial_code).lower().replace(" ", "_")
    if st.button(button, key=key):
        # Check answers
        if user_code == equals:
            if success:
                st.success(success)
            is_correct = True
        else:
            if error:
                st.error(error)
            is_correct = False
        # Save the answers, if required
        if "save_answers" in st.session_state and st.session_state.save_answers:                
            correct_answer = "Depends, dynamically generated"
            save_answer(question, is_correct=is_correct, user_answer=user_code, correct_answer=correct_answer)
        # Return if button is pressed and answer evaluation
        return True, is_correct
    else:
        # Return if button is not pressed
        return False, None