import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Tests")

# Streamit book properties
#stb.set_book_config(path="tests", button="top")

def header_test():
    st.caption("Header")
    #st.balloons()
    st.markdown("---")

def footer_test():
    st.markdown("---")
    st.caption("Footer")
    #st.balloons()

stb.set_book_config(path="tests", 
                    book_id="tests", 
                    #toc=True,
                    button="bottom",
                    username="sebastiandres", repository="streamlit-book",
                    #button_previous="Previous Page", button_next="Next Page", button_refresh="Refresh Page",
                    on_load_header=header_test,
                    on_load_footer=footer_test)