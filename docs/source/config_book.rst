Book configuration
==============================================

How does it works?
--------------------

Using the function `set_book_config`:

* Will setup a sidebar menu with each of the chapter.
* Each chapter is build with pagination for the provided file/folder.

The capability to render several chapters was added in version 0.7.0, and makes a direct use of 
`streamlit_option_menu` an awesome library to add a sidebar menu (`link <https://github.com/victoryhb/streamlit-option-menu>`_).
Kudos to the creator. It delivers a professional look, and being able to add `icons by name <https://icons.getbootstrap.com/>`_ makes it a lot more user-friendly. 

Required and optional arguments
--------------------------------

.. autofunction:: __init__.set_book_config



