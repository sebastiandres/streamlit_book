Introduction
============

streamlit_book is a (hopefully simpler) way to create streamlit apps using markdown and folder convention.

Capabilities
--------------------

* Reads all markdown and python files on the provided folder, allowing easy navigation
* Navigation: 
    * Select boxes on sidebar - based on the the file structure
    * Previous and next (customizable) buttons
* Bookmark button - save your last read page!
* Predefined activities: 
    * to do list 
    * true or false question
    * single choice question
    * multiple choice question
* Activities can be defined from plain markdown or from python functions

How does it works?
--------------------

* It will read the alphabetical order of the python and markdown files of the given path.
* It will read and render the files into streamlit, allowing a enriched markdown for pedagogical activities.

Why is it interesting?
-------------------------

Because a teacher does not need to (necesarily) know about streamlit to create a streamlit book. 
It only needs to create a folder structure and edit markdown files. 
And he even can add streamlit interactive apps, activities and quizzes!