import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Streamlit Book", page_icon="📖",)

# Streamit book properties
stb.set_library_config(menu_title="",
                       options=["Multitest", 
                                "To Do list", 
                                "True or False", 
                                "Multiple Choice", 
                                "Single Choice",
                                "Demo Day",
                                ], 
                       paths=["streamlit_book_examples/00 Multitest", 
                              "streamlit_book_examples/01 To do Lists", 
                              "streamlit_book_examples/02 True or False",
                              "streamlit_book_examples/03 Multiple choice",
                              "streamlit_book_examples/04 Single choice",
                              "streamlit_book_examples/DemoDay",                             
                              ],
                       icons=["code", 
                              "robot", 
                              "moon", 
                              "alarm", 
                              "activity", 
                              "apple",
                              ],
                       )