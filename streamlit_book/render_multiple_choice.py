import streamlit as st

from .keywords import *

def render_multiple_choice(lines):
    """
    """
    # Define default feedback messages 
    quizz = {
            SUCCESS:DEFAULT_SUCCESS_MESSAGE, 
            ERROR:DEFAULT_ERROR_MESSAGE, 
            BUTTON:DEFAULT_BUTTON_MESSAGE,
            "user_answers":[],
            "answers":[],
            }
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(MULTIPLE_CHOICE_KEYWORD):
                continue
            else:
                raise st.error(f"Error in the format.")
        elif line.startswith(MULTIPLE_CHOICE_TRUE):
            option_text = line[len(MULTIPLE_CHOICE_TRUE):].strip()
            user_answer = st.checkbox(option_text)
            quizz["user_answers"].append(user_answer)  
            quizz["answers"].append(True)   # The correct answer is True (selected)
        elif line.startswith(MULTIPLE_CHOICE_FALSE):
            option_text = line[len(MULTIPLE_CHOICE_FALSE):].strip()
            user_answer = st.checkbox(option_text)
            quizz["user_answers"].append(user_answer)  
            quizz["answers"].append(False)  # The correct answer is False (not selected)
        elif line.startswith(BUTTON):
            msg = line[len(BUTTON):].strip()
            quizz[BUTTON] = msg  
        elif line.startswith(SUCCESS):
            msg = line[len(SUCCESS):].strip()
            quizz[SUCCESS] = msg  
        elif line.startswith(ERROR):
            msg = line[len(ERROR):].strip()
            quizz[ERROR] = msg
        else:
            # Put the rest of the lines into header as markdown
            st.markdown(line)
    if len(quizz["answers"])>0:
        if st.button(quizz[BUTTON]):
            if all(u==a for u, a in zip(quizz["user_answers"], quizz["answers"])):
                st.success(quizz[SUCCESS])
            else:
                st.error(quizz[ERROR])
    return quizz