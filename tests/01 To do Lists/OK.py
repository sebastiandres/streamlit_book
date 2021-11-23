import streamlit as st
import streamlit_book as stb

st.title("Correct uses of stb.to_do_list")

st.caption("Test 01 - Minimal parameters")
stb.to_do_list(tasks={"a":True, "b":False, "c":True})

st.caption("Test 02 - All parameters")
stb.to_do_list(tasks={"a":True, "b":False, "c":False}, 
                header="Description 02",
                success="You did it!")

st.caption("Test 03 - All done")
stb.to_do_list(tasks={"a":True, "b":True, "c":True}, 
                header="Description 03")

st.caption("Test 02 - None done")
stb.to_do_list(tasks={"a":False, "b":False, "c":False}, 
                header="Description 04")

st.caption("Test 02 - Multiline markdown comment")
stb.to_do_list(tasks={"a":False, "b":False, "c":False}, 
                header="A very long multiline \n markdown \n comment")
