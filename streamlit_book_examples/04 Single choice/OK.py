import streamlit as st
import streamlit_book as stb

st.title("Correct uses of stb.single_choice")

st.caption("Test 01 - Minimal parameters")
stb.single_choice(question="Which is the current version of streamlit?",
                  options = ["0.0.1", "0.5.0", "1.0.1", "1.2.0"],
                  answer_index=3)