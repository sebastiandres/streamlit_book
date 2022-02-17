from streamlit_book.render_true_false import true_or_false

st.title("True or False - from a function")

st.subheader("Example with mandatory arguments:")

#with st.echo("below"):
st.code(
"""
question = "Is this a true or false statement?"
answer = True
true_or_false(question, answer)
"""
)
question = "Is this a true or false statement?"
answer = True
true_or_false(question, answer)

st.subheader("Example with all optional arguments:")

with st.echo("below"):
    question = "Is this a true or false statement?:"
    answer = False
    true_or_false(question, answer)
