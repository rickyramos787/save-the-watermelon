"""
logic.py

Contains the core game logic functions for Save the Watermelon.
"""


def display_word(secret_word, guessed_letters):
    """
    Return the secret word with guessed letters shown
    and unknown letters displayed as underscores.
    """
    output = []

    for letter in secret_word:
        if letter in guessed_letters:
            output.append(letter)
        else:
            output.append("_")

    return " ".join(output)


def is_word_guessed(secret_word, guessed_letters):
    """
    Return True if every letter in the secret word
    has been guessed. Otherwise, return False.
    """
