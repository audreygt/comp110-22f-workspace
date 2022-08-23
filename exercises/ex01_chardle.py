"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730545277"

character_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character: ")
print("Searching for " + single_character + " in " + character_word)
if single_character == str(character_word[single_character])

