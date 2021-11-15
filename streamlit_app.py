import streamlit as st
import pandas as pd
import numpy as np

DISPLAY_TEXT = "Display Text"
DISPLAY_DATA = "Display Data"

# Set wide display
st.set_page_config(layout="wide")

# Side Bar
## Create a page selector (radio or )
page = st.sidebar.radio("Choose your page:", 
                          [
                            DISPLAY_TEXT, 
                            DISPLAY_DATA, 
                            ]
                        ) 
## Links
links = [
        "* [Streamlit Cheat Sheet](https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py)",
        "* [Streamlit Gallery](https://streamlit.io/gallery)",
        ]
st.sidebar.markdown("Links:") 
st.sidebar.markdown("\n".join(links)) 

## Autor
st.sidebar.markdown("Created by [sebastiandres](https://sebastiandres.xyz)") 

if page == DISPLAY_TEXT:
    from pages import display_text
    display_text.display_page(DISPLAY_TEXT)
elif page == DISPLAY_DATA:
    from pages import display_data
    display_data.display_page(DISPLAY_DATA)