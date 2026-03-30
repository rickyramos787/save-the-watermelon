"""
words.py

Provides the word list and a function to choose a random word.
"""

import random

WORD_LIST = [
    "blanket",
    "summer",
    "picnic",
    "sunshine",
    "beach",
    "fruit",
    "garden",
    "harvest",
    "lemonade",
    "basket",
    "cantaloupe",
    "strawberry",
    "pineapple",
    "blueberry",
    "kiwi",
]


def choose_word():
    """
    Return one random word from the word list.
    """
    return random.choice(WORD_LIST)
