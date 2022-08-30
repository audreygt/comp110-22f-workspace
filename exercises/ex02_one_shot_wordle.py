"""Trying to complete this assignment better"""

__author__ = "730545277"

secret_word: str = "python"
guessed_word: str = input("What is your 6-letter guess?")
character_number: len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(guessed_word)!= character_number:
    print(f"That was not 6 letters! Try again: {guessed_word}")
    print("Not quite. Play again soon!")
    character_number = len(secret_word)

while len(guessed_word) == character_number:
    if guessed_word == secret_word:
        print("Woo! You got it!")