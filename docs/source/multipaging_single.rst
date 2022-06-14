Single page
-------------

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