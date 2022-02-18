from datetime import datetime
import streamlit as st
import subprocess
import os

ANSWER_FILENAME = "./tmp/answers.csv"

def get_git_revision_short_hash() -> str:
    """"
    Improved upon version found at 
    https://stackoverflow.com/questions/14989858/get-the-current-git-hash-in-a-python-script/21901260#21901260"
    """
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
    except:
        return "not_git"

def create_answer_file():
    if not os.path.exists(ANSWER_FILENAME):
        with open(ANSWER_FILENAME, "w") as f:
            f.write("commit_hash,datetime,user_id,question,correct?,user_answer,correct_answer\n")
        return

def save_answer(question, is_correct, user_answer, correct_answer):
    """
    Save the answer to the question.
    """
    print(os.path.abspath((ANSWER_FILENAME)))
    create_answer_file()
    commit_hash = st.session_state.commit_hash
    # datetime object containing current date and time
    dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    user_id = st.session_state.user_id
    # Clean question and answers
    question = question.replace("\n", "\\n")
    user_answer = str(user_answer).replace("\n", "\\n")
    correct_answer = str(correct_answer).replace("\n", "\\n")
    with open(ANSWER_FILENAME, "a") as f:
        f.write(f'"{commit_hash}","{dt_string}","{user_id}","{question}","{is_correct}","{user_answer}","{correct_answer}"\n')   
    return