Chapter: A single document with multiple connected pages
----------------------------------------------------------

* **Problem**: You want cute multipages, but you only need previous/next buttons.
* **Solution**: Use method `set_chapter_config`` to set the path and other chapter configurations.


.. code-block:: python

    import streamlit as st
    import streamlit_book as stb

    # Set wide display
    st.set_page_config()

    # Set multipage
    stb.set_chapter_config(path="pages/", save_answers=True)

Using the function `set_chapter_config`:

* Will setup the page navigation text/icons for a unique chapter.
* Will sort the python and markdown files of the given path on lexigraphic order.
* Will read and render the files into streamlit, allowing a enriched markdown/python of the implemented activities.

See the function `set_chapter_config` required and optional parameters on the :ref:`Multipaging Documentation`.

.. raw:: html

    <iframe src="https://stbook-multipaging.streamlitapp.com/chapter?embedded=true" width="700" height="700"></iframe>
    <br><br>