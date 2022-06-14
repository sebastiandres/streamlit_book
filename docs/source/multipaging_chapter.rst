Chapter: A single document with multiple connected pages
----------------------------------------------------------

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


How does it works?
~~~~~~~~~~~~~~~~~~~~

Using the function `set_chapter_config`:

* Will setup the page navigation text/icons for a unique chapter.
* Will sort the python and markdown files of the given path on lexigraphic order.
* Will read and render the files into streamlit, allowing a enriched markdown/python of the implemented activities.

Required and optional arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: __init__.set_chapter_config