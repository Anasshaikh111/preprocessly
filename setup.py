from setuptools import setup, find_packages

setup(
    name="preprocessly",
    version="0.2.0",
    packages=find_packages(),

    include_package_data=True,  # VERY IMPORTANT
    package_data={
        "preprocessly": ["*.json"],  # include all json files
    },

    install_requires=[
        "beautifulsoup4",
        "emoji",
        "nltk",
        "regex",
        "langdetect",
        "textblob"
    ],

    description="Advanced NLP preprocessing engine with spell correction, slang handling, contractions, profanity filtering and emoji normalization.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    python_requires=">=3.7",

    author="Ishaque Anas Shaikh",
    author_email="anasshaikh129229@gmail.com",
    url="https://github.com/Anasshaikh111/preprocessly",

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing :: Linguistic",
    ],
)
