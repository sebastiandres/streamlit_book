Types of configuration
===============================================

There are different needs addressed by the library.

Interactive single page
--------------------------------

You **don't** need multipages, but you want to reuse the activities/questions provided
by the library: easy, just import the library streamlit_book without the setup and call the required functions.


.. code-block:: python

    import streamlit as st
    import streamlit_book as stb

    st.set_page_config()

    # No need to initialize the streamlit_book library
    stb.true_or_false("Are you a robot?", False)

See this example 
(`streamlit app <https://share.streamlit.io/sebastiandres/stb_activities_demo_v070/main>`__, 
`github code <https://github.com/sebastiandres/stb_activities_demo_v070>`__) with different cases.

Chapter: A single document with multiple connected pages
---------------------------------------------------------

You need multipages, but you only need previous/next buttons.

Use stb.set_book_config to set the path and other book configurations.


.. code-block:: python

    import streamlit as st
    import streamlit_book as stb

    # Set wide display
    st.set_page_config()

    # Set multipage
    stb.set_chapter_config(path="pages/", save_answers=True)

See this example 
(`streamlit app <https://share.streamlit.io/sebastiandres/stb_chapter_demo_v070/main>`__, 
`github code <https://github.com/sebastiandres/stb_chapter_demo_v070>`__) with different cases.

Book: several simple or multipaged chapters
----------------------------------------------------

Requires a sidebar menu (like this demo), where each topic required a previous/next buttons.

Use `stb.set_book_config`` to set the path and the configuration for the book.


.. code-block:: python

    import streamlit as st
    import streamlit_book as stb

    # Streamlit webpage properties
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

See this example 
(`streamlit app <https://share.streamlit.io/sebastiandres/stb_book_demo_v070/main>`__, 
`github code <https://github.com/sebastiandres/stb_book_demo_v070>`__) with different cases.
