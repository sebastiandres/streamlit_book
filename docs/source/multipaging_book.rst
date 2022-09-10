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

Using the function `set_book_config`:

* Will setup a sidebar menu with each of the chapter.
* Each chapter is build with pagination for the provided file/folder.

The capability to render several chapters was added in version 0.7.0, and makes a direct use of 
an awesome library to add a sidebar menu called (`streamlit_option_menu <https://github.com/victoryhb/streamlit-option-menu>`_).
Kudos to the creator. It delivers a professional look, and allows to add `icons by name <https://icons.getbootstrap.com/>`_ makes it a lot more user-friendly. 

See the function `set_book_config` required and optional parameters on the :ref:`Multipaging Documentation`.

.. raw:: html

    <iframe src="https://stbook-multipaging.streamlitapp.com/book?embedded=true" width="700" height="700"></iframe>
    <br><br>