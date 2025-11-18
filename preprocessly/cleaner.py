import re
import string
import json
import emoji
import nltk
import unicodedata
from langdetect import detect
from textblob import TextBlob
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

from .utils import normalize_whitespace, load_json_dict, load_list


class Preprocessly:
    def __init__(
        self,
        remove_stopwords=False,
        do_lemmatize=False,
        do_stem=False,
        emoji_to_text=False,
        correct_spelling=False,
        detect_language=True,
        clean_profanity=False
    ):

        # flags
        self.remove_stopwords_flag = remove_stopwords
        self.do_lemmatize_flag = do_lemmatize
        self.do_stem_flag = do_stem
        self.correct_spelling_flag = correct_spelling
        self.emoji_to_text_flag = emoji_to_text
        self.detect_language_flag = detect_language
        self.clean_profanity_flag = clean_profanity

        # nltk downloads
        nltk.download("stopwords", quiet=True)
        nltk.download("wordnet", quiet=True)

        # resources
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()
        self.contractions = load_json_dict("contractions.json")
        self.slang = load_json_dict("slang.json")
        self.bad_words = load_list("profanity_list.txt")

    # -------- BASIC CLEANERS -------- #

    def remove_html(self, text):
        return BeautifulSoup(text, "html.parser").get_text()

    def remove_urls(self, text):
        return re.sub(r"https?://\S+|www\.\S+", "", text)

    def remove_usernames(self, text):
        return re.sub(r"@\w+", "", text)

    def remove_hashtags(self, text):
        return re.sub(r"#\w+", "", text)

    def remove_emojis(self, text):
        return emoji.replace_emoji(text, replace="")

    def emojis_to_text(self, text):
        return emoji.demojize(text, delimiters=(" ", " "))

    def remove_punctuation(self, text):
        return text.translate(str.maketrans("", "", string.punctuation))

    def unicode_normalize(self, text):
        return unicodedata.normalize("NFKD", text)

    def to_lower(self, text):
        return text.lower()

    # -------- TEXT NORMALIZATION -------- #

    def expand_contractions(self, text):
        for c, full in self.contractions.items():
            text = text.replace(c, full)
        return text

    def normalize_slang(self, text):
        words = text.split()
        return " ".join(self.slang.get(w, w) for w in words)

    def remove_profanity(self, text):
        return " ".join("" if w in self.bad_words else w for w in text.split())

    def correct_spelling(self, text):
        return str(TextBlob(text).correct())

    def normalize_numbers(self, text):
        # example "10k" -> "10000"
        text = re.sub(r"(\d+)k\b", lambda m: str(int(m.group(1)) * 1000), text)
        return text

    # -------- LINGUISTIC CLEANUP -------- #

    def remove_stopwords(self, text):
        return " ".join(
            word for word in text.split() if word not in self.stop_words
        )

    def lemmatize_text(self, text):
        return " ".join(
            self.lemmatizer.lemmatize(word) for word in text.split()
        )

    def stem_text(self, text):
        return " ".join(self.stemmer.stem(word) for word in text.split())

    # -------- MASTER CLEAN METHOD -------- #

    def clean(self, text):
        text = str(text)

        # Language detection
        if self.detect_language_flag:
            try:
                lang = detect(text)
            except:
                lang = "unknown"

            if lang != "en":
                return f"[Unsupported language: {lang}]"

        # Core cleaning
        text = self.unicode_normalize(text)
        text = self.remove_html(text)
        text = self.remove_urls(text)
        text = self.remove_usernames(text)
        text = self.remove_hashtags(text)

        if self.emoji_to_text_flag:
            text = self.emojis_to_text(text)
        else:
            text = self.remove_emojis(text)

        text = self.to_lower(text)
        text = self.expand_contractions(text)
        text = self.normalize_slang(text)
        text = self.normalize_numbers(text)
        text = normalize_whitespace(text)

        if self.clean_profanity_flag:
            text = self.remove_profanity(text)

        # remove punctuation
        text = self.remove_punctuation(text)

        # advanced
        if self.correct_spelling_flag:
            text = self.correct_spelling(text)

        if self.remove_stopwords_flag:
            text = self.remove_stopwords(text)

        if self.do_lemmatize_flag:
            text = self.lemmatize_text(text)

        if self.do_stem_flag:
            text = self.stem_text(text)

        text = normalize_whitespace(text)
        return text
