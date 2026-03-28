# Save the Watermelon - Pseudocode

## Main Game Flow
```python
FUNCTION main
    DISPLAY welcome message
    SET play_again = "yes"
    WHILE play_again is "yes"
        CALL play_game
        ASK player if they want to play again
        CONVERT answer to lowercase
        WHILE answer is not "yes" AND answer is not "no"
            DISPLAY "Please enter yes or no."
            ASK again
            CONVERT answer to lowercase
