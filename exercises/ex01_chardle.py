"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730545277"

instances: int = 0
typed_word: str = input("Enter a 5-character word: ")
if len(typed_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(typed_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

typed_character: str = input("Enter a single character: ")
if len(typed_character) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(typed_character) < 1: 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + typed_character + " in " + typed_word)

if typed_word[0] == typed_character:
    print(typed_character + " found at index 0")
    instances = instances + 1
if typed_word[1] == typed_character: 
    print(typed_character + " found at index 1")
    instances = instances + 1
if typed_word[2] == typed_character:
    print(typed_character + " found at index 2")
    instances = instances + 1
if typed_word[3] == typed_character:
    print(typed_character + " found at index 3")
    instances = instances + 1
if typed_word[4] == typed_character:
    print(typed_character + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + typed_character + " found in " + typed_word)
else: 
    if instances == 1: 
        print("1 instance of " + typed_character + " found in " + typed_word)
    else:
        if instances == 2: 
            print("2 instances of " + typed_character + " found in " + typed_word)
        else:
            if instances == 3: 
                print("3 instances of " + typed_character + " found in " + typed_word)
            else:
                if instances == 4: 
                    print("4 instances of " + typed_character + " found in " + typed_word)
                else: 
                    if instances == 5: 
                        print("5 instances of " + typed_character + " found in " + typed_word)