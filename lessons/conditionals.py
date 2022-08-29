"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number 1-5, what is it?")
guess: int = (int(input("What is your guess? ")))

if guess == SECRET: 
    print("You guessed correctly!!!")
    print("You did great, have a wonderful day!!!")
else:
    print("Sorry, you guess incorrectly :(")
    if guess > SECRET:
        print("Try a lower number.")
    else:
        print("Try a higher number.")

print("Game over.")