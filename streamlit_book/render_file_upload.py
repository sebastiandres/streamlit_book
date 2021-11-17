import streamlit as st

from .keywords import *

def render_file_upload(lines):
    """
    """
    KEYWORD = "#file-upload"
    EXPLANATION = "explanation:"
    true_solution_dict = {}
    explanation = ""
    for i, line in enumerate(lines):
        if i==0:
            continue
        elif line.startswith(EXPLANATION):
            explanation = line[len(EXPLANATION):].strip()
            true_solution_dict["explanation"] = explanation  
        else:
            question = line
            key = line.lower().replace(" ","")
            st.markdown(question)
    st.file_uploader("")
    return