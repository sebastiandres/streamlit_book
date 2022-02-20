import os
import pandas as pd
import streamlit as st

try:
    from helpers import get_datetime_string, download_file, get_token
    from keywords import USERS_FILENAME, ANSWER_FILENAME
except: 
    from .helpers import get_datetime_string, download_file, get_token
    from .keywords import USERS_FILENAME, ANSWER_FILENAME

def create_user_df(user_id, token):
    """
    Create a dataframe with the user information.
    """
    dt_string = get_datetime_string()
    user_df = pd.DataFrame(columns=["user_id", "token", "datetime"], data=[[user_id, token, dt_string]])
    return user_df

def get_user_from_token(query_token):
    df = pd.read_csv(USERS_FILENAME)
    m = df["token"] == query_token
    if m.any():
        user_for_token = df.user_id[m].values[0] # the first (and only) one
        return user_for_token
    else:
        return None

def create_new_user_and_token():
    """
    Returns the user id and token.
    """
    # Create folder, if not there
    try:
        os.mkdir("./tmp/")
    except:
        pass
    # Check for user file, create if not there
    if not os.path.exists("./tmp/users.csv"):
        df0 = create_user_df(0,"abc123")
        df0.to_csv(USERS_FILENAME, index=False)
    # Take a new user
    df_users = pd.read_csv(USERS_FILENAME)
    user_id = df_users["user_id"].max() + 1
    user_token = get_token()
    df_new_user = create_user_df(user_id, user_token)
    df_users = pd.concat([df_users, df_new_user])
    df_users.to_csv(USERS_FILENAME, index=False)
    # Create the token
    return (user_id, user_token)

def get_token_from_user(user_id):
    df = pd.read_csv(USERS_FILENAME)
    m = df["user_id"] == user_id
    if m.any():
        token = df.token[m].values[0]
        return token
    else:
        return None