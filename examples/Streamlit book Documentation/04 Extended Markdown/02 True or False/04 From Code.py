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
if True:
    question = "Is this a true or false statement?"
    answer = True
    true_or_false(question, answer)

st.subheader("Example with all optional arguments:")

with st.echo("below"):
    question = "Is this a true or false statement?"
    answer = True
    true_or_false(question+":", answer, 
                    success="Bien", error="Mal", button="Click")
