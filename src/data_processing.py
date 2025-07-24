"""
Utility functions for text processing.
"""

# Imports

import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

# Tokenization and processing


def process(text):
    """
    Process the text in several steps:
    _ word tokenization;
    _ removing all punctuation and digits;
    _ removing stop words;
    _ lemmatization.
    """
    # Get tokens
    tokens = word_tokenize(text)
    # Keep only words
    only_words = [re.sub(r"[^a-zA-Z ]", "", w) for w in tokens]
    # Remove stop words and write all in lowercase
    stop_words = set(stopwords.words("english"))
    only_relevant_words = [
        w.lower() for w in only_words if w.lower() not in stop_words and w != ""
    ]
    # Lemmatize
    wnl = WordNetLemmatizer()
    return " ".join([wnl.lemmatize(w) for w in only_relevant_words])
