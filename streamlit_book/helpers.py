from datetime import datetime
import streamlit as st
import subprocess
import random
import os

try:
    from keywords import ADMIN_PASSWORD
except: 
    from .keywords import ADMIN_PASSWORD

def password_entered():
    """
    Checks whether a password entered by the user is correct.
    Checks agains secrets (if defined) otherwise checks against hardcoded password.
    """
    # Get the password
    try:
        PASSWORD = st.secrets["ADMIN_PASSWORD"]
    except:
        PASSWORD = ADMIN_PASSWORD
    # Compare against password entered by the user
    if st.session_state["password"] == PASSWORD:
        st.session_state["password_correct"] = True
        del st.session_state["password"]  # don't store password
    else:
        st.session_state["password_correct"] = False
    # Delete password from session state
    del PASSWORD
    return

def password_login(user_id):
    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")

def get_datetime_string():
    # datetime object containing current date and time
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt_string

def get_git_revision_short_hash() -> str:
    """"
    Improved upon version found at 
    https://stackoverflow.com/questions/14989858/get-the-current-git-hash-in-a-python-script/21901260#21901260"
    """
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
    except:
        return "not_git"

def download_file(df, button_label, filename, where=None):
    """
    """
    data_csv = df.to_csv().encode('utf-8')
    if where:
        btn = where.download_button(
                label=button_label,
                data=data_csv,
                file_name=filename,
            )
    else:
        btn = st.download_button(
                label=button_label,
                data=data_csv,
                file_name=filename,
            )
    return

def get_token():
    t1 = get_random_string(3, "letters")
    t2 = get_random_string(3, "numbers")
    return t1 + t2

def get_random_string(length, elements):
    if elements == "letters":
        elements = "abcdefghkmnopqrstxyz" # no confusing characters
    elif elements == "numbers":
        elements = "0123456789"
    else:
        elements = string.digits + string.ascii_letters
    # With combination of lower and upper case
    result_str = ''.join(random.choice(elements) for i in range(length))
    # print random string
    return result_str