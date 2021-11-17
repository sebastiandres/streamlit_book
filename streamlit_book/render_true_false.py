import streamlit as st
import glob

from .keywords import *

def render_true_or_false(lines):
    """
    """
    # Define default feedback messages 
    quizz = {
            SUCCESS:DEFAULT_SUCCESS_MESSAGE, 
            ERROR:DEFAULT_ERROR_MESSAGE, 
            BUTTON:DEFAULT_BUTTON_MESSAGE,
            }
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(TRUE_FALSE_KEYWORD):
                continue
            else:
                raise st.error(f"Error in the format.")
        elif i==1:
            question = line
            key = line.lower().replace(" ","")
        elif i==2:
            answer = line.strip()
            if answer in ("True", "False"):
                quizz["answer"] = answer
            else:
                raise st.error(f"Answer must be True or False. Got {answer}")
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
            st.markdown(line)
    # If there is a question, create the radio question
    if question:
        user_answer = st.radio(question, options=["True", "False"], key=key)
        if st.button(quizz[BUTTON]):
            if user_answer == quizz["answer"]:
                st.success(quizz[SUCCESS])
            else:
                st.error(quizz[ERROR])
    return quizz
