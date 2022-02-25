To do list
================

This functionality allows to create to-do list. 
It only has as optional argument the text for success.

Python
--------

.. autofunction:: __init__.to_do_list


An example code for a to-do list is:

.. code-block:: python

    stb.to_do_list({"task 1":True, "task 2":False, "task 3":False})
                   header="A (completely optional) description for the to do list:", 
                   succes="Congrats! You did it!"
                  )

Markdown
--------

The to-do list follows the standard Markdown syntax.

.. code-block:: none

    stb.to_do_list
    A (completely optional) description for the to do list:
    - [x] task 1
    - [ ] task 1
    - [ ] task 3
    succes: Congrats! You did it! 

The success text will get rendered on a st.success element when completing the tasks. If not provided, it just returns a default success message.

Example
--------

.. image:: _images/to_do_list.gif
  :width: 800
  :alt: Rendering of to_do_list