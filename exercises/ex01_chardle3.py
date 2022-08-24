"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730545277"

from operator import countOf


typed_word: str = input("Enter a 5-character word: ")
LIMIT: int = 5
if len(typed_word) >= LIMIT:
    print("Error: Word must contain 5 characters")

typed_character: str = input("Enter a single character: ")
print("searching for " + typed_character + " in " + typed_word)
LIMIT: int = 1
if len(typed_character) >= LIMIT:
    print("Error: Character must be a single character.")

if typed_word[0] == typed_character:
    print(typed_character + " found at index 0")
else:
    if typed_word[1] == typed_character: 
        print(typed_character + " found at index 1")
    else:
        if typed_word[2] == typed_character:
            print(typed_character + " found in index 2")
        else: 
            if typed_word[3] == typed_character:
                print(typed_character + " found in index 3")
            else:
                if typed_word[4] == typed_character:
                    print(typed_character + " found in index 4")

MATCH: int = 1
if (countOf[typed_character]) == MATCH:
    print("1 instances of " + typed_character + " in " + typed_word)
else:
    MATCH: int = 2
    if typed_word(countOf[typed_character]) == MATCH:
        print("2 instances of " + typed_character + " in " + typed_word)
    else: 
        MATCH: int = 0
        if typed_word(countOf[typed_character]) == MATCH:
            print("No instances of" + typed_character + " found in " + typed_word)

