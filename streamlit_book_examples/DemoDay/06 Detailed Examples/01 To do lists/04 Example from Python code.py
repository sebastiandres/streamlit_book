from streamlit_book.render_to_do_list import to_do_list

st.title("To do list from a function")

st.subheader("Example with mandatory arguments:")

with st.echo("below"):
    to_do_list( {
                "a":True, "b":False, "c":True}, 
            )

st.subheader("Example with all optional arguments:")

with st.echo("below"):
    to_do_list( {
                "a":True, "b":False, "c":True}, 
                header="To do list"
            )