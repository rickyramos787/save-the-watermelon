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


def prompt_for_guess(guessed_letters):
    """
    Prompt the player until they enter a valid guess.
    Return the valid lowercase letter.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()
        is_valid, message = validate_guess(guess, guessed_letters)

        if is_valid:
            return guess

        print(message)


def prompt_play_again():
    """
    Ask the player whether they want to play again.
    Return 'yes' or 'no'.
    """
    while True:
        answer = input("Would you like to play again? (yes/no): ").strip().lower()        

        if answer in ("yes", "no"):
            return answer

        print("Please enter yes or no.")


def play_game():
    """
    Run one full round of the game.
    """
    secret_word = choose_word()
    guessed_letters = set()
    slices = STARTING_SLICES

    print("\nWelcome to Save the Watermelon!")
    print("Guess the word one letter at a time before the watermelon runs out of slices.")

    while slices > 0 and not is_word_guessed(secret_word, guessed_letters):
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Guessed letters:", display_guessed_letters(guessed_letters))
        print("Slices remaining:", slices)
