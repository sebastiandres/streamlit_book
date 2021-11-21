# Library to configure this setup file
from distutils.core import setup

# Import the version of the the pypsdier
from streamlit_book import version as current_version
print("Current Library Version:", current_version)

# Use the README for the long description
long_description=open('README.mds').read()

setup(
    name='streamlit_book',
    version=current_version,
    author='Sebastian Flores Benner',
    author_email='sebastiandres@gmail.com',
    packages=['streamlit_book'],
    scripts=[],
    url='https://github.com/sebastiandres/streamlit_book',
    license='MIT',
    description='A streamlit companion library to create a interactive reader for the content on a given folder.',
    long_description=long_description,
    install_requires=[streamlit],
    )
