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
        END WHILE
        SET play_again = answer
    END WHILE
    DISPLAY goodbye message
END FUNCTION


## Play One Round

FUNCTION play_game
    SET secret_word = choose_word()
    SET guessed_letters = empty set
    SET slices = 6

    WHILE slices > 0 AND word is not fully guessed
        DISPLAY current masked word
        DISPLAY guessed letters
        DISPLAY remaining slices

        SET guess = prompt_for_guess()

        IF guess is already in guessed_letters
            DISPLAY "You already guessed that letter."
            CONTINUE loop
        END IF

        ADD guess to guessed_letters

        IF guess is in secret_word
            DISPLAY "Nice! That letter is in the word."
        ELSE
            SUBTRACT 1 from slices
            DISPLAY "Wrong guess."
        END IF
    END WHILE

    DISPLAY final version of the word

    IF word is fully guessed
        DISPLAY win message
    ELSE
        DISPLAY lose message
        DISPLAY secret word
    END IF
END FUNCTION


## Choose a Word

FUNCTION choose_word
    RETURN one random word from the word list
END FUNCTION


## Show Masked Word

FUNCTION display_word(secret_word, guessed_letters)
    SET output = empty string

    FOR each letter in secret_word
        IF letter is in guessed_letters
            ADD letter to output
