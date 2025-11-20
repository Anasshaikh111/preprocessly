# preprocessly
Advanced NLP preprocessing engine with spell correction, slang handling, contractions, profanity filtering and emoji normalization.

Preprocessly is a modern, modular, and highly extensible text preprocessing engine designed for real-world AI/ML applications, LLM pipelines, RAG systems, and NLP workflows.

It cleans raw, messy text and transforms it into high-quality, normalized input ready for embeddings, transformers, classical ML models, or downstream NLP tasks.

## Features
### 1. Text Cleaning

Remove HTML tags

Remove URLs

Remove mentions (@user)

Remove hashtags (#topic)

Normalize whitespace

Unicode normalization

Lowercasing

Remove punctuation

### 2. NLP-Level Normalization

Contraction expansion (don’t → do not)

Slang normalization (u → you, brb → be right back)

Number normalization (10k → 10000)

Language detection (auto)

Optional profanity filtering

Optional spell correction

### 3. AI-Enhanced Processing

Lemmatization

Stemming

Stopword removal

Emoji handling (remove or convert to text)

Custom plugin-based extensibility

Emoji handling (remove or convert to text)

Custom plugin-based extensibility


## Installation
#### pip install preprocessly

## How to Use preprocessly
You only need one main function:

#### import preprocessly as pp
#### cleaned_text = pp.clean("your text here")
