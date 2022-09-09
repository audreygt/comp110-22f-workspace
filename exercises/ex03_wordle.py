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
checking: int = 0
right_character: bool = False
emoji_answer: str = ""

def emojified(guessed_word: str, secret_word: str) -> str:
    """testing for the indexes using colored boxes"""
    assert len(guessed_word) == len(secret_word)
    contains_char(guessed_word, secret_word)
    while contains_char is True:
        emoji_answer += GREEN_BOX
    while contains_char is False and checking < len(guessed_word):
        if secret_word[checking] == guessed_word[index]:
            right_character = True 
            checking += 1
        if right_character is not True:
            emoji_answer += WHITE_BOX
        else:
            emoji_answer += YELLOW_BOX
    return emoji_answer

