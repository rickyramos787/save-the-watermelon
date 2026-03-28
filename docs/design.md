# Save the Watermelon - Design

## Problem Statement
Save the Watermelon is a terminal-based word guessing game where the player tries to reveal a hidden word by guessing one letter at a time. The goal is to guess the full word before the watermelon loses all of its slices. This game is meant for users who want a simple, interactive console game with clear rules and input prompts.

## Target Audience
The target audience is beginner-level players and students learning basic Python programming concepts. The game is designed to be easy to understand, easy to run, and simple to play in a terminal window.

## Game Rules
- The game randomly selects one secret word from a word list.
- The player guesses one letter at a time.
- If the guessed letter is in the secret word, all matching positions are revealed.
- If the guessed letter is not in the secret word, the player loses one slice.
- The player cannot guess the same letter more than once.
- The player must enter only one alphabetical character at a time.
- The player wins if all letters in the secret word are revealed before the slices reach 0.
- The player loses if the slices reach 0 before the word is completed.

## Win and Lose Conditions
### Win Condition
The player wins when every letter in the secret word has been guessed correctly.

### Lose Condition
The player loses when the remaining slice count reaches 0 before finishing the word.

## Core Features (Must-Have)
- Random word selection
- Masked word display
- Letter-by-letter guessing
- Slice counter
- Input validation
- Repeated guess detection
- Win/lose detection
- Replay option

## Stretch Goals (Nice-to-Have)
- ASCII art showing watermelon slices
- Difficulty levels
- Word categories
- Hint system
- Scoreboard for multiple rounds

## Basic Game Flow
1. Start the game.
2. Select a secret word randomly.
3. Set the number of slices.
4. Show the masked version of the word.
5. Ask the player to guess a letter.
6. Validate the input.
7. Check whether the letter was already guessed.
8. If the guess is correct, reveal matching letters.
9. If the guess is incorrect, subtract one slice.
10. Check for win or lose condition.
11. Repeat until the player wins or loses.
12. Ask if the player wants to play again.
13. End or restart the game.

14. ## Data Design
The program will store:
- **Secret word** as a string
- **Guessed letters** as a set
- **Revealed word state** as a generated display string
- **Remaining slices** as an integer
- **Word list** as a list of strings

Using a set for guessed letters makes it easy to check for duplicates quickly. A string list or generated display can be used to show progress after each guess.

## Module Responsibilities

### `src/game.py`
This file will handle the main game loop, player interaction, replay logic, and displaying messages to the user.

### `src/logic.py`
This file will handle the core game functions, such as checking guesses, revealing letters, validating win conditions, and updating slices.

### `src/words.py`
This file will provide the word list and the function used to choose a random secret word.

## Function Responsibility Plan
Possible functions include:
- `choose_word()` - selects a random word
- `display_word(secret_word, guessed_letters)` - returns the masked word display
