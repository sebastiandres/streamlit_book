True or False question
=========================

This functionality allows to ask a True or False question. 
It requires a question and a the solution as True/False value. 
Optionally, the success, failure and button can be customized.

Python
--------

.. autofunction:: __init__.true_or_false

Markdown
--------

Format for questions where expected answer is True

.. code-block:: none

    stb.true_or_false
    Question description
    True

Format for questions where expected answer is False

.. code-block:: none

    stb.true_or_false
    Question description
    False

Optional arguments

* `success:` This will get rendered on a st.success element if answer is correct. If not provided, it just returns a default success message.
* `failure:` This will get rendered on a st.failure element if answer is wrong. If not provided, it just displays "Wrong answer".
* `button:` Alternative text for the button. If not provided, it displays "Check answer'. 

Example
--------

A complete format for true-or-false is as follows:

.. code-block:: none

    stb.true_or_false
    Is "Indiana Jones and the Last Crusade" one of the best movies?
    True
    success: You have chosen wisely
    failure: You chose poorly
    button: You must choose