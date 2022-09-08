"""Creating wordle for the 3rd time."""

__author__ = "730545277"

secret_word: str = "codes"
emojis: str = ""
def contains_char(guessed_word: str, guessed_character: str) -> bool:
    """finding the character in the word"""
    assert len(guessed_character) == 1
    index: int = 0

    while index < len(guessed_word):
        if guessed_character == guessed_word[index]:
            return True
        else:
            index += 1
    return False 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
right_character: bool = False

def emojified(guessed_word: str, typed_word: str) -> str:
    """testing for the indexes using colored boxes"""
    assert len(guessed_word) == len(typed_word)
    while len(guessed_word) == len(typed_word):
        if guessed_word[index] == typed_word[index]:
            return GREEN_BOX
    if guessed_word[index] != typed_word[index]:
        while right_character is not True and checking < len(guessed_word):
            if typed_word[checking] == guessed_word[index]:
                right_character = True 
            checking += 1
        if right_character is not True:
            return WHITE_BOX
        else:
            return YELLOW_BOX

def input_guess(n: int) -> str:
    """allowing user multiples tried until correct length"""
    if 