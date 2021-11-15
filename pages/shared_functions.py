import streamlit as st

def breakline():
    st.markdown("---")
    return    

def documentation(function):
    breakline()
    st.markdown(f"Documentation: [link](https://docs.streamlit.io/en/stable/api.html#streamlit.{function})")
    return