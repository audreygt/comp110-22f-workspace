"""Trying to complete this assignment better."""

__author__ = "730545277"

secret_word: str = "coffeecake"
character_number = len(secret_word)
guessed_word: str = input(f"What is your {character_number}-letter guess? ")
index: int = 0
checking: int = 0
response_answer: str = ""
running_times: int = len(secret_word)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guessed_word) != character_number:
    guessed_word = input(f"That was not {character_number} letters! Try again: ")

if len(guessed_word) == len(secret_word) and guessed_word != secret_word:
    while index < character_number:
        checking = 0
        right_character: bool = False 
        if guessed_word[index] == secret_word[index]:
            response_answer += GREEN_BOX
        if guessed_word[index] != secret_word[index]:
            while right_character is not True and checking < len(guessed_word):
                if secret_word[checking] == guessed_word[index]:
                    right_character = True 
                checking += 1
            if right_character is not True:
                response_answer += WHITE_BOX
            else:
                response_answer += YELLOW_BOX
        index += 1 
    print(response_answer)   
    print("Not quite. Play again soon!")

if guessed_word == secret_word:
    print("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9")
    print("Woo! You got it!")