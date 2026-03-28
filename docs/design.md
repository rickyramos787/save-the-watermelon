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
