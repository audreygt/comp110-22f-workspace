"""Creating wordle for the 3rd time."""

__author__ = "730545277"

from xmlrpc.client import boolean


secret_word: str = "python"
word_length: len(secret_word)
index: int = 0


def contains_char(guessed_word, guessed_character) -> boolean:

    assert len(guessed_word) == 1
    if guessed_character == guessed_word[index]:
        while index < word_length:
            index += 1
        return True
    else:
        return False 

guessed_word: str = (input(f"Enter a {word_length} character word: "))
guessed_character: str = (input("Enter a character."))
