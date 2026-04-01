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
