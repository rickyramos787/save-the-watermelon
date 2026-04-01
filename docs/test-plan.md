# Save the Watermelon - Test Plan

## Purpose
The purpose of this test plan is to verify that Save the Watermelon works correctly during normal gameplay and handles invalid input properly.

## Manual Test Cases

### Test Case 1: Valid Lowercase Input
**Action:** Enter one lowercase letter, such as `a`  
**Expected Result:** The guess is accepted and processed correctly.

### Test Case 2: Valid Uppercase Input
**Action:** Enter one uppercase letter, such as `B`  
**Expected Result:** The input is converted to lowercase and processed correctly.

### Test Case 3: Number Input
**Action:** Enter a number, such as `4`  
**Expected Result:** The program rejects the input and displays an error message.

### Test Case 4: Symbol Input
**Action:** Enter a symbol, such as `@`  
**Expected Result:** The program rejects the input and displays an error message.

### Test Case 5: Multiple Characters
**Action:** Enter more than one character, such as `ab`  
**Expected Result:** The program rejects the input and displays an error message.
the input and displays an error message.

### Test Case 6: Blank Input
**Action:** Press Enter without typing a letter  
**Expected Result:** The program rejects the input and displays an error message.

### Test Case 7: Repeated Guess
**Action:** Enter a valid letter, then enter the same letter again  
**Expected Result:** The second guess is rejected with a repeated guess message.

### Test Case 8: Correct Guess
**Action:** Enter a letter that is in the secret word  
**Expected Result:** The letter is revealed in all correct positions and slices do not decrease.

### Test Case 9: Incorrect Guess
**Action:** Enter a letter that is not in the secret word  
**Expected Result:** A message is displayed and the slice count decreases by 1.

### Test Case 10: Win Condition
**Action:** Guess all letters in the secret word before slices reach 0  
**Expected Result:** The program displays a win message.

### Test Case 11: Lose Condition
**Action:** Continue making incorrect guesses until slices reach 0  
**Expected Result:** The program displays a lose message and shows the secret word.

### Test Case 12: Replay With Yes
**Action:** After the game ends, enter `yes`  
**Expected Result:** A new round starts.

### Test Case 13: Replay With No
**Action:** After the game ends, enter `no`  
**Expected Result:** The program ends with a goodbye message.

### Test Case 14: Invalid Replay Input
**Action:** After the game ends, enter something other than `yes` or `no`  
**Expected Result:** The program asks the player to enter yes or no.

## Testing Summary
The game was manually tested for:
- valid inputs
- invalid inputs
- repeated guesses
