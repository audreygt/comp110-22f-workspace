"""Creating wordle for the 3rd time."""

__author__ = "730545277"


def contains_char(guessed_word: str, guessed_character: str) -> bool:
    """Finding the character in the word."""
    assert len(guessed_character) == 1
    index: int = 0
    while index < len(guessed_word):
        if guessed_character == guessed_word[index]:
            return True
        else:
            index += 1
    return False 


def emojified(guessed_word: str, secret_word: str) -> str:
    """Providing hints for guessed word."""
    assert len(guessed_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    contains: bool = True 
    emoji_answer: str = ""
    guessed_character = guessed_word[index]
    contains_char(guessed_word, guessed_character)
    while index < len(guessed_word):
        if guessed_word[index] == secret_word[index]:
            emoji_answer += GREEN_BOX
        if guessed_word[index] != secret_word[index] and contains == contains_char(secret_word, guessed_word[index]):
            emoji_answer += YELLOW_BOX
        if guessed_word[index] != secret_word[index] and contains != contains_char(secret_word, guessed_word[index]):
            emoji_answer += WHITE_BOX
        index += 1 
    return emoji_answer 


def input_guess(length_expected: int) -> str:
    """Testing the length of guessed word."""
    secret_word: str = "simoncelli"
    guessed_word: str = input(f"Enter a {len(secret_word)} character word: ")
    expected_length: int = len(guessed_word)
    while expected_length != len(secret_word):
        guessed_word = input(f"That wasn't {len(secret_word)} chars! Try again: ")
        expected_length = len(guessed_word)
    return str(guessed_word)


def main() -> None:
    """The entry point of the program and main game."""
    secret_word: str = "simoncelli"
    play_number: int = 1
    limit_number: int = 20
    playing: bool = True
    while play_number <= limit_number and playing is True: 
        print(f"=== Turn {play_number}/20 ===")
        guessed_word = input_guess(len(secret_word))
        print(emojified(guessed_word, secret_word))
        if guessed_word == secret_word: 
            print(f"You won in {play_number}/{limit_number} turns.")
            playing = False
        else: 
            play_number += 1
    if playing:
        print("X/6 - Sorry, try again tomorrow.")
    return None


if __name__ == "__main__":
    secret_word: str = "simoncelli"
    main()
