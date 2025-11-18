from setuptools import setup, find_packages

setup(
    name="preprocessly",
    version="0.2.0",
    packages=find_packages(),

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

    python_requires=">=3.8",
)
