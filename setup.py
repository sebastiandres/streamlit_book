from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-slides",
    version="0.7.8",
    author="Sebastián Flores Benner",
    author_email="sebastiandres@gmail.com",
    description="A streamlit companion library to create a interactive reader for the content on a given folder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sebastiandres/streamlit_book",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
        'streamlit-option-menu',
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.36.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    }
)