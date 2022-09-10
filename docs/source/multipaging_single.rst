Single page
-------------

* **Problem**: You have one page to show, but you want to use the activities/questions provided on streamlit_book.
* **Solution**: Just import the library streamlit_book without the setup and call the required functions.

.. code-block:: python

    import streamlit as st
    import streamlit_book as stb

    st.set_page_config()

    # No need to initialize the streamlit_book library
    stb.true_or_false("Are you a robot?", False)

.. raw:: html

    <iframe src="https://stbook-multipaging.streamlitapp.com/single?embedded=true" width="700" height="700"></iframe>
    <br><br>