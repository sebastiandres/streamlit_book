import streamlit as st

try:
    from keywords import *
except:
    from .keywords import *

def file_upload_from_lines(lines):
    """Parses the line into a dictionary of values of interest.

    :param lines: list of lines
    :type lines: list
    :return: Returns a dict of the parsed values for the file upload.
    :rtype: dict
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