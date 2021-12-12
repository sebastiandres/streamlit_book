Multiple choice question
===========================

Markdown
----------

.. code-block:: none

    stb.multiple_choice
    Question
    [T] True option
    [F] False option
    [T] Another true option
    [F] Another false option 1
    [F] Another false option 2

Optional configurations
* `success:` This will get rendered on a st.success element if answer is wrong. If not provided, it just returns a default success message.
* `failure:` This will get rendered on a st.failure element if answer is wrong. If not provided, it just displays "Wrong answer".
* `button:` Alternative text for the button. If not provided, it displays "Check answer'. 

Python
--------

.. autofunction:: __init__.multiple_choice

Example
---------

.. code-block:: none

    stb.multiple-choice
    Which of the following are python libraries?
    [T] streamlit
    [F] pikachu
    [T] numpy
    [F] psyduck
    [T] matplotlib