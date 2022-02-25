# streamlit_book

[![Open in Streamlit][share_badge]][share_link]

`streamlit_book` is a streamlit companion library, written in python+streamlit to create a interactive reader for the content on a given folder. It was developed on November 2021 during streamlit's hackathon - ended up being awarded one of the two best apps!

## Demos

The list of all demos of the library for release 0.7.0. are:

* [Demo Activities v0.7.0](https://share.streamlit.io/sebastiandres/stb_activities_demo_v070/main): how activities can be used without multipage capability.
* [Demo Chapter v0.7.0](https://share.streamlit.io/sebastiandres/stb_chapter_demo_v070/main): Using a chapter (previous/next pagination).
* [Demo Book v0.7.0](https://share.streamlit.io/sebastiandres/stb_book_demo_v070/main): Using a book (sidebar navigation on chapters).

## Examples 

Some apps using the library are:

* [Happy Birds](https://share.streamlit.io/sebastiandres/streamlit_happy_birds/main/happy_birds.py) : A self contained example that mixes features of the library with a funny twist.
* [The (confusion) Matrix](https://share.streamlit.io/sebastiandres/ml-edu-1-confusion-matrix/main): Take the blue pill to learn all about the confusion matrix.
* [The Streamlitsaurus Rex](https://share.streamlit.io/sebastiandres/streamlit_datasaurus/main/app.py): Will teach you to always visualize your data, and exhibits the mythical Datasaurus.

## Documentation

All the documentation is at [readthedocs](https://streamlit_book.readthedocs.io/).

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

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/sebastiandres/stb_book_demo_v070/main