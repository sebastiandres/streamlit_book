# streamlit_book

`streamlit_book` is a streamlit companion library, written in python+streamlit to create a interactive reader for the content on a given folder. It was developed on November 2021 during streamlit's hackathon - ended up being awarded one of the two best apps!

## Documentation

All the documentation is at [readthedocs](https://streamlit-book.readthedocs.io/en/latest).

## Demos

The list of all demos of the library for release 0.7.0. are:

* [Demo Methods](https://stbook-methods.streamlit.app/): differente activities and methods. 
* [Demo Multipaging](https://stbook-multipaging.streamlit.app/): Different multipaging options (native and stbook).

## Examples 

Some apps using the library are:

* [Happy Birds](https://notangrybirds.streamlit.app/) : A self contained example that mixes features of the library with a funny twist.
* [The (confusion) Matrix](https://confusion-matrix.streamlit.app/): Take the blue pill to learn all about the confusion matrix.
* [The Streamlitsaurus Rex](https://datasaurus.streamlit.app/): Will teach you to always visualize your data, and exhibits the mythical Datasaurus.

## How to use it

Install it:

```bash
pip install streamlit_book
```

There are [different ways to use it](https://streamlit-book.readthedocs.io/en/latest/config.html), but in short just add to `streamlit_app.py` the function that list the files to be read (and other properties):

```python
import streamlit as st
import streamlit_book as stb

# Streamlit page properties
st.set_page_config()

# Streamit book properties
stb.set_book_config(menu_title="streamlit_book",
                    menu_icon="lightbulb",
                    options=[
                            "What's new on v0.7.0?",
                            "Core Features",
                            ],
                    paths=[
                          "pages/00_whats_new.py", # single file
                          "pages/01 Multitest", # a folder
                          ],
                    icons=[
                          "code",
                          "robot",
                          ],
                    save_answers=True,
                    )
```


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=sebastiandres/streamlit_book&type=Date)](https://star-history.com/#sebastiandres/streamlit_book&Date)
