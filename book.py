import streamlit as st
from streamlit_book import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide")

# Streamit book properties
stb.set_book_config(path="examples")
#stb.set_book_config(path="examples/empty_example")
#stb.set_book_config(path="examples/math_book")
#stb.set_book_config(path="examples/documentation")
#stb.set_book_config(path="examples/debug")

## Autor
st.sidebar.markdown("Created by [sebastiandres](https://sebastiandres.xyz)")