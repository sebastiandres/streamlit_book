Share on Social Media
======================

You can create share buttons for social media. This is based on the code I found at https://sharingbuttons.io/, 
which after a couple of hours of googling turned out to be the simplest way to share the content. 
Kudos to creator. It has some minor modifications, but it's mostly a wrapping of the code for stremlit.

It requires as arguments the message and the url.

Python
--------

.. autofunction:: __init__.share


Markdown
--------

.. code-block:: none

    stb.share
    Some text
    http://www.some-url.com


Example
--------

.. image:: _images/share.png
  :width: 800
  :alt: Rendering of share buttons