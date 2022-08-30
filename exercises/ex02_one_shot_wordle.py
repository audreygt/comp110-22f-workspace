"""Trying to complete this assignment better"""

__author__ = "730545277"

secret_word: str = "python"
character_number = len(secret_word)
guessed_word: str = input("What is your 6-letter guess? ")
index: int = 0
wrong_character: bool = False 
right_character: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guessed_word) != character_number:
    guessed_word = input("That was not 6 letters! Try again: ")

if len(guessed_word) == len(secret_word) and guessed_word != secret_word:
    while index < character_number:
        print("Not quite. Play again soon!")

if guessed_word == secret_word:
    while index < character_number:
        if guessed_word[index] == secret_word[index]:
            index = index + 1
    print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print("Woo! You got it!")