# Library to configure this setup file
import pathlib
from setuptools import find_packages, setup

# VERSION - is a variable that is defined in the __init__.py file
VERSION = "0.4.6"

HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = 'streamlit_book' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Sebastian Flores Benner'
AUTHOR_EMAIL = 'sebastiandres@gmail.com'
URL = 'https://github.com/sebastiandres/streamlit_book'

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'A streamlit companion library to create a interactive reader for the content on a given folder.'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"
PROJECT_URLS = {
                "Documentation": "https://streamlit-book.readthedocs.io/",
                'Source': 'https://github.com/sebastiandres/streamlit_book/',
                'Tracker': 'https://github.com/sebastiandres/streamlit_book/issues',
                }
# Libraries required by the package
INSTALL_REQUIRES = ['streamlit']

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    include_package_data=True,    
    url=URL,
    project_urls=PROJECT_URLS,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    setup_requires=INSTALL_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    )
