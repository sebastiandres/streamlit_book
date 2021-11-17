# How to use it

As usual, create a `requirements.txt` with the required libraries, making sure to include `streamlit` and `streamlit_book`.

Create and maintain your files in a folder structure, where you can use markdown (md) and Python files (py).

Create a Python file where you point to the correct path:

```python
import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide")

# Streamit book properties
stb.set_book_config(path="example")
```