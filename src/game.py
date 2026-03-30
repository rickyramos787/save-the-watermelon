"""
game.py

Main game loop for Save the Watermelon.
"""

from src.words import choose_word
from src.logic import (
    display_word,
    is_word_guessed,
    display_guessed_letters,
    validate_guess,
    process_guess,
)


STARTING_SLICES = 6
