import streamlit as st

try:
    from keywords import check_keyword
    from keywords import MULTIPLE_CHOICE_KEYWORD, MULTIPLE_CHOICE_FALSE, MULTIPLE_CHOICE_TRUE
    from keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
    from answers import save_answer
except:
    from .keywords import check_keyword
    from .keywords import MULTIPLE_CHOICE_KEYWORD, MULTIPLE_CHOICE_FALSE, MULTIPLE_CHOICE_TRUE
    from .keywords import BUTTON, SUCCESS, ERROR, DEFAULT_SUCCESS_MESSAGE, DEFAULT_ERROR_MESSAGE, DEFAULT_BUTTON_MESSAGE
    from .answers import save_answer


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
    :return: tuple of booleans with button press status and correctness of answer
    :rtype: tuple of bool
    """
    cb_list = []
    if len(question)==0:
        st.error("Please provide a question")
        return None, None
    elif len(options_dict)<2:
        st.error("Must have at least 2 options")
        return None, None
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
            # Check answers
            if all(u==a for u, a in zip(cb_list, options_dict.values())):
                if success:
                    st.success(success)
                is_correct = True
            else:
                if error:
                    st.error(error)
                is_correct = False
            # Save the answers, if required
            if "save_answers" in st.session_state and st.session_state.save_answers:                
                user_answer = [list(options_dict.keys())[i] for i, cb in enumerate(cb_list) if cb]
                correct_answer = [key for key, val in options_dict.items() if val]
                save_answer(question, is_correct=is_correct, user_answer=user_answer, correct_answer=correct_answer)
            # Return if button is pressed and answer evaluation
            return True, is_correct
        else:
            # Return if button is not pressed
            return False, None