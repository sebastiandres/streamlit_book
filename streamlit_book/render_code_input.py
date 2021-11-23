import streamlit as st

try:
    from keywords import *
except:
    from .keywords import *

def code_input_from_lines(lines):
    """Parses a list of lines into a dictionary with the parsed values.

    :param lines: list of lines
    :type lines: list
    :return: dict of the parsed values for the code input quizz type.
    :rtype: dict
    """    # Define default feedback messages 
    quizz = {
            SUCCESS:DEFAULT_SUCCESS_MESSAGE, 
            ERROR:DEFAULT_ERROR_MESSAGE, 
            BUTTON:DEFAULT_BUTTON_MESSAGE,
            "question":"",
            "answer_check":{},
            }
    # Iterate through lines and process each line accordingly
    for i, line in enumerate(lines):
        if i==0:
            if line.startswith(CODE_INPUT_KEYWORD):
                continue
            else:
                raise st.error(f"Error in the format.")
        elif line.startswith(EXACT_TEXT):
            msg = line[len(EXACT_TEXT):].strip()
            quizz["answer_check"][EXACT_TEXT] = msg
        elif line.startswith(CONTAINS_TEXT):
            msg = line[len(CONTAINS_TEXT):].strip()
            quizz["answer_check"][CONTAINS_TEXT] = msg
        elif line.startswith(STARTS_WITH):
            msg = line[len(STARTS_WITH):].strip()
            quizz["answer_check"][STARTS_WITH] = msg
        elif line.startswith(ENDS_WITH):
            msg = line[len(ENDS_WITH):].strip()
            quizz["answer_check"][ENDS_WITH] = msg
        elif line.startswith(ASSERT):
            msg = line[len(ASSERT):].strip()
            quizz["answer_check"][ASSERT] = msg
        elif line.startswith(BUTTON):
            msg = line[len(BUTTON):].strip()
            quizz[BUTTON] = msg
        elif line.startswith(SUCCESS):
            msg = line[len(SUCCESS):].strip()
            quizz[SUCCESS] = msg  
        elif line.startswith(ERROR):
            msg = line[len(ERROR):].strip()
            quizz[ERROR] = msg
        else:
            # Add the line to question text
            quizz["question"] += line

    # Create the quiz
    user_answer = st.text_area(quizz["question"])
    if st.button(quizz[BUTTON]):
        st.write(user_answer)
        if passes_all_tests(user_answer, quizz):
            st.success(quizz[SUCCESS])
        else:
            st.error(quizz[ERROR])
    return

def passes_all_tests(user_answer, quizz):
    """
    """
    check_list = []
    if EXACT_TEXT in quizz["answer_check"]:
        check_list.append(user_answer.strip()==quizz["answer_check"][EXACT_TEXT].strip())
    if CONTAINS_TEXT in quizz["answer_check"]:
        check_list.append(quizz["answer_check"][CONTAINS_TEXT] in user_answer)
    if ENDS_WITH in quizz["answer_check"]:
        check_list.append(user_answer.endswith(quizz["answer_check"][ENDS_WITH]))
    if STARTS_WITH in quizz["answer_check"]:
        check_list.append(user_answer.startswith(quizz["answer_check"][STARTS_WITH]))
    if ASSERT in quizz["answer_check"]:
        try:
            assert(exec(quizz["answer_check"][ASSERT]))
            check_list.append(True)
        except:
            st.error(f"Assertion failed: {quizz['answer_check'][ASSERT]}")
            check_list.append(False)
    return all(check_list)