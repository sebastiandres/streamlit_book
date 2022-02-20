import streamlit as st
import os
import pandas as pd
import altair as alt
try:
    from keywords import USERS_FILENAME, ANSWER_FILENAME
    from helpers import password_login, download_file, get_git_revision_short_hash
except: 
    from .keywords import USERS_FILENAME, ANSWER_FILENAME, ADMIN_PASSWORD
    from .helpers import password_login, download_file, get_git_revision_short_hash

def admin_page():
    """"
    Shows a password page to the admin.
    """
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        admin_login_page()
    else:
        c1, c2 = st.columns(2)
        c1.title("Admin page")
        # Show configuration
        options = ["Configuration", "User info", "Answer info"]
        option = c2.selectbox("Choose an option", options)
        # Show users
        if option == options[0]:
            configuration()
        if option == options[1]:
            user_info()
        if option == options[2]:
            answers_info()
    return

def configuration():
    """
    Shows available info on users.
    """
    st.header("Configuration")
    c1, c2, c3 = st.columns(3)
    c1.metric(label="Save answers?", value=f"{st.session_state.save_answers}")
    commit_hash = get_git_revision_short_hash()
    c2.metric(label="Current commit", value=f"{commit_hash}")


def user_info():
    """
    Shows available info on users.
    """
    if os.path.exists(USERS_FILENAME):
        # If file exists, read the file
        df = pd.read_csv(USERS_FILENAME)
        # Provide some basic stats
        n_users = len(df)
        first_user = df.datetime.min()
        last_user = df.datetime.max()
        c1, c2, c3 = st.columns(3)
        c1.metric(label="# users", value=f"{n_users}")
        c2.metric(label="First user created on", value=f"{first_user}")
        c3.metric(label="Last user created on", value=f"{last_user}")
        # Plot the users by day
        df['day'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S").dt.strftime('%Y-%m-%d')
        alt_df = df.groupby("day").count().rename(columns={"user_id": "# users"}).reset_index()
        alt_plot = alt.Chart(alt_df).mark_line(point=alt.OverlayMarkDef(color="blue")).encode(x="day", y="# users")
        #st.write(alt_df)
        st.altair_chart(alt_plot)
        # Allow to download the file
        download_file(df, button_label="Download user data", filename="users.csv")
        # Show the file or a graph
        #st.write(df)
    else:
        st.warning("No users file found.")    

def answers_info():
    """
    Shows available info on answers.
    """
    # Show answers
    if os.path.exists(ANSWER_FILENAME):
        df = pd.read_csv(ANSWER_FILENAME)
        # Provide some basic stats
        n_answers = len(df)
        n_unique_users = df["user_id"].nunique()
        n_unique_questions = df["question"].nunique()
        correctness = df["correct?"].mean()
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(label="# answers", value=f"{n_answers}")
        c2.metric(label="# users on answers", value=f"{n_unique_users}")
        c3.metric(label="# questions", value=f"{n_unique_questions}")
        c4.metric(label="Average correct?", value=f"{100*correctness}%")
        # Plot the users by day
        df['day'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S").dt.strftime('%Y-%m-%d')
        alt_df = df.groupby("day").count().rename(columns={"user_id": "# users"}).reset_index()
        alt_plot = alt.Chart(alt_df).mark_line(point=alt.OverlayMarkDef(color="blue")).encode(x="day", y="# users")
        #st.write(alt_df)
        st.altair_chart(alt_plot)
        # Allow to download the file
        c1, c2 = st.columns(2)
        df_last_answer = df.drop_duplicates(keep="last")
        download_file(df, "Download all answers", "all_answers.csv", where=c1)
        download_file(df_last_answer, "Download last answers", "last_answers.csv", where=c2)
        # Show the file or a graph
        #st.write(df)
    else:
        st.warning("No answers file found.")

def admin_login_page():
    """"
    Shows a password page to the admin.
    """
    st.title("Admin Login")
    st.write("Please enter the password to access the admin page.")
    password_login("admin")