Single choice question
========================

Markdown
--------

.. code-block:: none

    stb.single_choice
    Which is the current version of streamlit?
    - 0.0.1
    - 0.5.5
    + 1.2.0
    - 9.9.9

Optional configurations

* `success:` This will get rendered on a st.success element if answer is wrong. If not provided, it just returns a default success message.
* `failure:` This will get rendered on a st.failure element if answer is wrong. If not provided, it just displays "Wrong answer".
* `button:` Alternative text for the button. If not provided, it displays "Check answer'. 

Python
-------

.. autofunction:: __init__.single_choice

Markdown
--------

.. code-block:: none

    stb.single_choice
    Which is the current version of streamlit?
    - 0.0.1
    - 0.5.5
    + 1.2.0
    - 9.9.9