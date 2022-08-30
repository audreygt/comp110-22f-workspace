"""Trying to complete this assignment better"""

__author__ = "730545277"

secret_word: str = "python"
character_number = len(secret_word)
guessed_word: str = input("What is your 6-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guessed_word) != character_number:
    guessed_word = input("That was not 6 letters! Try again: ")
    



   