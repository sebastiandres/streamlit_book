import streamlit as st

from .keywords import *

def render_single_choice(lines):
    """
    """
    # Define default feedback messages 
    quizz = {
            SUCCESS:DEFAULT_SUCCESS_MESSAGE, 
            ERROR:DEFAULT_ERROR_MESSAGE, 
            BUTTON:DEFAULT_BUTTON_MESSAGE,
            "answer_options":[],
            "true_answer":"",
            "answer":"",
            "question":"",
            }
    # Save space for warnings
    st_placeholder = st.empty()
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(SINGLE_CHOICE_KEYWORD):
                continue
            else:
                raise st.error(f"Error in the format.")
        elif line.startswith(SINGLE_CHOICE_CORRECT):
            option_text = line[len(SINGLE_CHOICE_CORRECT):].strip()
            quizz["answer_options"].append(option_text)
            if quizz["true_answer"] == "":
                quizz["true_answer"] = option_text
            else:
                st_placeholder.error(f"FORMAT ERROR. Check the markdown for this activity. More than one correct answer.")
        elif line.startswith(SINGLE_CHOICE_WRONG):
            option_text = line[len(SINGLE_CHOICE_WRONG):].strip()
            quizz["answer_options"].append(option_text)
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
            quizz["question"] += line
    if len(quizz["question"])>0 and len(quizz["answer_options"])>0:
        user_answer = st.radio(quizz["question"], 
                                options=quizz["answer_options"])
        if st.button(quizz[BUTTON]):
            if user_answer == quizz["true_answer"]:
                st.success(quizz[SUCCESS])
            else:
                st.error(quizz[ERROR])
    # If no option is correct, display a warning message
    if quizz["true_answer"]=="":
        st_placeholder.error("FORMAT ERROR. Check the markdown for this activity. No correct answer has been defined.")
    return quizz