import streamlit as st
import streamlit_book as stb

st.title("Wrong uses of stb.to_do_list")

st.caption("Test 01 - No parameters")
try:
    stb.to_do_list()
except Exception as e:
    st.exception(e)


st.caption("Test 02 - Empty list")
try:
    stb.to_do_list(tasks={})
except Exception as e:
    st.exception(e)