import streamlit as st
import os

try:
    from helpers import get_datetime_string, get_git_revision_short_hash
    from keywords import ANSWER_FILENAME 
except: 
    from .helpers import get_datetime_string, get_git_revision_short_hash
    from .keywords import ANSWER_FILENAME 

def create_answer_file():
    if not os.path.exists(ANSWER_FILENAME):
        with open(ANSWER_FILENAME, "w") as f:
            f.write("commit_hash,datetime,user_id,question,correct?,user_answer,correct_answer\n")
        return

def save_answer(question, is_correct, user_answer, correct_answer):
    """
    Save the answer to the question.
    """
    # Parameters
    create_answer_file()
    commit_hash = st.session_state.commit_hash
    dt_string = get_datetime_string()
    user_id = st.session_state.user_id
    # Clean question and answers
    question = question.replace("\n", "\\n")
    user_answer = str(user_answer).replace("\n", "\\n")
    correct_answer = str(correct_answer).replace("\n", "\\n")
    with open(ANSWER_FILENAME, "a") as f:
        f.write(f'"{commit_hash}","{dt_string}","{user_id}","{question}","{is_correct}","{user_answer}","{correct_answer}"\n')   
    return