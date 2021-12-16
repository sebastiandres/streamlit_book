
def check_keyword(line, keyword):
    """
    Check if the line starts with the keyword
    Replaces - for _ for backwards compatibility.
    """
    new_line = line.replace("-", "_")
    return new_line.startswith(keyword)

TODO_KEYWORD = "stb.to_do"
TODO_COMPLETED = "- [x] "
TODO_INCOMPLETE = "- [ ] "
TODO_SUCCESS = "Bravo!"

TRUE_FALSE_KEYWORD = "stb.true_or_false"

SINGLE_CHOICE_KEYWORD = "stb.single_choice"
SINGLE_CHOICE_CORRECT = "+ "
SINGLE_CHOICE_WRONG = "- "

MULTIPLE_CHOICE_KEYWORD = "stb.multiple_choice"
MULTIPLE_CHOICE_TRUE = "[T] "
MULTIPLE_CHOICE_FALSE = "[F] "

TEXT_INPUT_KEYWORD = "stb.text_input"

CODE_INPUT_KEYWORD = "stb.code_input"

FILE_UPLOAD_KEYWORD = "stb.file_upload"

BUTTON = "button:"
DEFAULT_BUTTON_MESSAGE = "Check answer"
SUCCESS = "success:"
DEFAULT_SUCCESS_MESSAGE = "Correct answer"
ERROR = "error:"
DEFAULT_ERROR_MESSAGE = "Wrong answer"

EXACT_TEXT = "equals:"
CONTAINS_TEXT = "contains:"
STARTS_WITH = "starts_with:"
ENDS_WITH = "ends_with:"

ASSERT = "assert:"
