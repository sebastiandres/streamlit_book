import streamlit as st
import streamlit_book as stb

st.markdown("# Python: Testing all the components")

st.markdown("---")
stb.to_do_list(tasks={"a":True, "b":False, "c":False}, 
                header="Description 02",
                success="You did it!")

st.markdown("---")
stb.true_or_false("Question description", False)

st.markdown("---")
stb.single_choice("Select the correct answers", ["a", "b", "c"], 0)

st.markdown("---")
stb.multiple_choice("Select the correct answers", {"a":True, "b":False, "c":False})

st.markdown("---")
stb.share("My blog", "http://sebastiandres.xyz")