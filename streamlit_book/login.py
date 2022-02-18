import os
import pandas as pd
import streamlit as st

def password_entered():
    """Checks whether a password entered by the user is correct."""
    if st.session_state["password"] == "123": #st.secrets["password"]:
        st.session_state["password_correct"] = True
        del st.session_state["password"]  # don't store password
    else:
        st.session_state["password_correct"] = False

def password_login(user_id):
    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")

def admin_page():
    """"
    Shows a password page to the admin.
    """
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        admin_login_page()
    else:
        st.title("Admin page")
        # Show configuration
        st.write("Configuration:")
        st.write(f"User login: {st.session_state.user_login}")
        st.write(f"Save answers: {st.session_state.save_answers}")
        # Show users
        with st.expander("Users"):
            if os.path.exists("./tmp/users.csv"):
                df_users = pd.read_csv("./tmp/users.csv")
                st.write(df_users)
            else:
                st.warning("No users file found.")
        # Show answers
        with st.expander("Answers"):
            if os.path.exists("./tmp/answers.csv"):
                df_users = pd.read_csv("./tmp/answers.csv")
                st.write(df_users)
            else:
                st.warning("No answers file found.")


def admin_login_page():
    """"
    Shows a password page to the admin.
    """
    st.title("Admin Login")
    st.write("Please enter the password to access the admin page.")
    password_login("admin")

def user_login_page():
    """"
    Shows a password page to the admin.
    """
    st.title("User Login")
    st.write("Please enter the password to access the admin page.")
    user_id = st.text_input("User ID", key="user_id")
    password_login("user")


def create_user_df(user_id, name):
    """
    Create a dataframe with the user information.
    """
    user_df = pd.DataFrame(columns=["user_id", "user_name"], data=[[user_id, name]])
    return user_df

def get_current_user_id():
    """
    Returns the current user id.
    """
    # Create folder, if not there
    try:
        os.mkdir("./tmp/")
    except:
       pass
    # Check for user file, create if not there
    if not os.path.exists("./tmp/users.csv"):
        df0 = create_user_df(0, "Admin")
        df0.to_csv("./tmp/users.csv", index=False)
    # Take a new user
    df_users = pd.read_csv("./tmp/users.csv")
    user_id = df_users["user_id"].max() + 1
    df_new_user = create_user_df(user_id, "Lorem Ispum")
    df_users = pd.concat([df_users, df_new_user])
    df_users.to_csv("./tmp/users.csv", index=False)
    return user_id
