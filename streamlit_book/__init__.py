import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# The version of the library
try:
    ### The main function to be used to read the files
    from file_reader import set_book_config
    # Some additional interesting functions
    from render_true_or_false import true_or_false
    from render_to_do_list import to_do_list
    from render_single_choice import single_choice
    from render_multiple_choice import multiple_choice
    #from render_text_input import text_input
    #from render_code_input import code_input
    #from render_file_upload import file_upload
except:
    ### The main function to be used to read the files
    from .file_reader import set_book_config
    # Some additional interesting functions
    from .render_true_or_false import true_or_false
    from .render_to_do_list import to_do_list
    from .render_single_choice import single_choice
    from .render_multiple_choice import multiple_choice
    #from .render_text_input import text_input
    #from .render_code_input import code_input
    #from .render_file_upload import file_upload



