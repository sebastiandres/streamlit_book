# streamlit_book

`streamlit_book` is a streamlit companion library, written in python+streamlit to create a interactive reader for the content on a given folder. It was developed on November 2021 during streamlit's hackathon - ended up being awarded one of the two best apps!

## Documentation

All the documentation is at [readthedocs](https://streamlit_book.readthedocs.io/).

## Examples 

* [Streamlit Book Examples](https://share.streamlit.io/sebastiandres/streamlit_book_examples/main/book.py): Several different examples.
* [Happy Birds](https://share.streamlit.io/sebastiandres/streamlit_happy_birds/main/happy_birds.py): A small explanation on trajectory motion.

## How to use it

Install it:

```bash
pip install streamlit_book
```

Create a file that references the folder with the files you want to render as a book:

```python
import streamlit as st
import streamlit_book as stb

# Streamlit properties
st.set_page_config(layout="wide", page_title="My page title")

# Streamit book properties
stb.set_book_config(path="my/path")
```