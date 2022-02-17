import streamlit as st
import streamlit_book as stb

st.title("Correct uses of stb.single_choice")

st.caption("Test 01 - Minimal parameters")
stb.multiple_choice(question="Which of the following are python libraries?",
                    options_dict = {"streamlit":True, 
                                "pikachu":False,
                                "numpy":True,
                                "psyduck":False,
                                "matplotlib":True})
