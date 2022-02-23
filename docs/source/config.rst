A Streamlit Book
===============================================

There are different needs addressed by the library.

Basic or interactive single page
--------------------------------

You **don't** need multipages, but you want to reuse the activities/questions provided
by the library: easy, just import the library streamlit_book without the setup and call the required functions.


.. code-block::python
    import streamlit as st
    import streamlit_book as stb

    st.set_config()

    st.title("Please answer this question")
    if stb.single_choice("What is your favorite color?", ["Red", "Blue", "Green"], 0):
        st.write("You chose Red")
    else:
        st.write("You chose Blue or Green")

Chapter: A single document with multiple connected pages
---------------------------------------------------------

You need multipages, but you only need previous/next buttons.

Use stb.set_book_config to set the path and other book configurations.


.. code-block::python
    import streamlit as st
    import streamlit_book as stb

    st.set_config()

    stb.set_chapter_config(path="pages/")

Book: several simple or multipaged chapters
----------------------------------------------------

Requires a sidebar menu (like this demo), where each topic required a previous/next buttons.

Use `stb.set_book_config`` to set the path and the configuration for the book.


.. code-block::python
    import streamlit as st
    import streamlit_book as stb

    st.set_config()

    stb.set_book_config(


    )