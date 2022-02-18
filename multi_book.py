import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Streamlit Book", page_icon="📖",)

c1, c2, c3 = st.columns(3)
user_login = c1.checkbox("Login", False)
save_answers = c2.checkbox("Save answers", False)

# Streamit book properties
stb.set_library_config(menu_title="",
                       options=[
                                "Intro",   
                                "Multitest", 
                                "To Do list", 
                                "True or False", 
                                "Multiple Choice", 
                                "Single Choice",
                                "Demo Day",
                                "End",   
                                ], 
                       paths=[
                              "streamlit_book_examples/Intro.py", 
                              "streamlit_book_examples/00 Multitest", 
                              "streamlit_book_examples/01 To do Lists", 
                              "streamlit_book_examples/02 True or False",
                              "streamlit_book_examples/03 Multiple choice",
                              "streamlit_book_examples/04 Single choice",
                              "streamlit_book_examples/DemoDay",                             
                              "streamlit_book_examples/End.md", 
                              ],
                       icons=["tree", 
                              "code", 
                              "robot", 
                              "moon", 
                              "alarm", 
                              "activity", 
                              "apple",
                              "tree",
                              ],
                       user_login=user_login,
                       save_answers=save_answers,
                       )