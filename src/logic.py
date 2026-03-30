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
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def display_guessed_letters(guessed_letters):
    """
    Return guessed letters in sorted order as a string.
    Return 'None' if no letters have been guessed.
    """
    if not guessed_letters:
        return "None"
    return ", ".join(sorted(guessed_letters))


def validate_guess(guess, guessed_letters):
    """
    Validate the player's guess.

    Returns a tuple:
    (is_valid, message)

    Rules:
    - must be exactly one character
    - must be alphabetical
    - must not already be guessed
    """
    guess = guess.strip().lower()

    if len(guess) != 1:
        return False, "Enter exactly one letter."

    if not guess.isalpha():
        return False, "Enter a letter from A to Z only."

    if guess in guessed_letters:
        return False, "You already guessed that letter."

    return True, ""


def process_guess(secret_word, guess, guessed_letters, slices):
    """
    Process a guess and return updated values.

    Returns:
    (message, new_slices)

    Assumes the guess has already been validated.
    """
    guessed_letters.add(guess)

    if guess in secret_word:
        return "Nice! That letter is in the word.", slices

    return "Wrong guess. You lost a slice.", slices - 1
