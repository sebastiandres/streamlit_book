import contextlib
import re
import textwrap
import traceback
from typing import List, Iterable, Optional

_SPACES_RE = re.compile("\\s*")
_EMPTY_LINE_RE = re.compile("\\s*\n")

@contextlib.contextmanager
def echo(code_location="above", show=True):
    """Whether to show the echoed code before or after the results of the executed code block.
    :param code_location: "above" or "below"
    :type lines: str
    :param show: Boolean to show or hide the code block
    :type lines: bool
    :return: None
    :rtype: none
    Copied and improved from `Streamlit's github <https://github.com/streamlit/streamlit/blob/d44b162909fb8adcae463172c78000029e5d2fef/lib/streamlit/echo.py>`_
    """

    from streamlit import code, warning, empty, source_util

    if code_location == "below":
        show_code = code
        show_warning = warning
    else:
        placeholder = empty()
        show_code = placeholder.code
        show_warning = placeholder.warning

    try:
        # Get stack frame *before* running the echoed code. The frame's
        # line number will point to the `st.echo` statement we're running.
        frame = traceback.extract_stack()[-3]
        filename, start_line = frame.filename, frame.lineno

        # Read the file containing the source code of the echoed statement.
        with source_util.open_python_file(filename) as source_file:
            source_lines = source_file.readlines()

        # Get the indent of the first line in the echo block, skipping over any
        # empty lines.
        initial_indent = _get_initial_indent(source_lines[start_line:])

        # Iterate over the remaining lines in the source file
        # until we find one that's indented less than the rest of the
        # block. That's our end line.
        #
        # Note that this is *not* a perfect strategy, because
        # de-denting is not guaranteed to signal "end of block". (A
        # triple-quoted string might be dedented but still in the
        # echo block, for example.)
        # TODO: rewrite this to parse the AST to get the *actual* end of the block.
        lines_to_display: List[str] = []
        for line in source_lines[start_line:]:
            indent = _get_indent(line)
            if indent is not None and indent < initial_indent:
                break
            lines_to_display.append(line)

        code_string = textwrap.dedent("".join(lines_to_display))

        # Run the echoed code...
        yield

        # And draw the code string to the app!
        if show: # Improvement: only show if required!!!
            show_code(code_string, "python")

    except FileNotFoundError as err:
        show_warning("Unable to display code. %s" % err)



def _get_initial_indent(lines: Iterable[str]) -> int:
    """Return the indent of the first non-empty line in the list.
    If all lines are empty, return 0.
    """
    for line in lines:
        indent = _get_indent(line)
        if indent is not None:
            return indent

    return 0


def _get_indent(line: str) -> Optional[int]:
    """Get the number of whitespaces at the beginning of the given line.
    If the line is empty, or if it contains just whitespace and a newline,
    return None.
    """
    if _EMPTY_LINE_RE.match(line) is not None:
        return None

    match = _SPACES_RE.match(line)
    return match.end() if match is not None else 0