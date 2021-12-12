import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Tests")

# Streamit book properties
#stb.set_book_config(path="tests", button="top")
stb.set_book_config(path="tests", toc=True, username="sebastiandres", repository="streamlit-book")