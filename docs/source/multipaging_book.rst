Book: Having several chapters
-------------------------------

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

How does it works?
~~~~~~~~~~~~~~~~~~~~

Using the function `set_book_config`:

* Will setup a sidebar menu with each of the chapter.
* Each chapter is build with pagination for the provided file/folder.

The capability to render several chapters was added in version 0.7.0, and makes a direct use of 
`streamlit_option_menu` an awesome library to add a sidebar menu (`link <https://github.com/victoryhb/streamlit-option-menu>`_).
Kudos to the creator. It delivers a professional look, and being able to add `icons by name <https://icons.getbootstrap.com/>`_ makes it a lot more user-friendly. 

Required and optional arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: __init__.set_book_config



