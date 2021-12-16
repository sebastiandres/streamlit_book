import streamlit as st
import streamlit_book as stb

# Streamlit webpage properties
st.set_page_config(layout="wide", page_title="Tests")

# Streamit book properties
#stb.set_book_config(path="tests", button="top")

def on_next_click2():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number + 1) % st.session_state.total_files
    st.write("next", st.session_state.file_number)
    return

def on_previous_click2():
    """
    Updates the values of update_from_selectbox and update_from_button.
    Updates the page number to +1, or 0 if the last page was reached.
    """
    st.session_state.file_number = (st.session_state.file_number - 1) % st.session_state.total_files
    st.write("previous", st.session_state.file_number)
    return

stb.set_book_config(path="tests", toc=True, 
                    username="sebastiandres", repository="streamlit-book",
                    on_next_click=on_next_click2)