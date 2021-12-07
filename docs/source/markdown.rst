Markdown syntax
================

The following Markdown syntax should be used to generate
the desired quiz and activities.

To do list
----------

.. code-block:: none

    stb.to_do
    [Optional] Description:
    [x] task 1
    [ ] task 1
    [ ] task 3


True or False question
-----------------------

Format for questions where expected answer is True

.. code-block:: none

    stb.true-false
    Question description
    True

Format for questions where expected answer is False

.. code-block:: 

    stb.true-false
    Question description
    False

Single choice question
-------------------------

.. code-block:: none

    stb.single-choice
    Which is the current version of streamlit?
    - 0.0.1
    - 0.5.5
    + 1.2.0
    - 9.9.9

Multiple choice question
-------------------------

.. code-block:: none

    stb.multiple-choice
    Which of the following are python libraries?
    [T] streamlit
    [F] pikachu
    [T] numpy
    [F] psyduck
    [T] matplotlib

Optional configurations
------------------------

Questions and to-do can be configured with the following optional parameter:

* `success:` This will get rendered on a st.success element if answer is wrong. If not provided, it just returns a default success message.

Questions (but not to-do) can be configured with the following optional parameters:

* `failure:` This will get rendered on a st.failure element if answer is wrong. If not provided, it just displays "Wrong answer".
* `button:` Alternative text for the button. If not provided, it displays "Check answer'. 

A complete format for true-or-false is as follows:

.. code-block:: none

    stb.true-false
    Is "Indiana Jones and the Last Crusade" one of the best movies?
    True
    success: You have chosen wisely
    failure: You chose poorly
    button: You must choose