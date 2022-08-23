
SECRET: int = 2

user_name = input("What is your name?")
guess: int = (int(input("On a scale of 1 to 10, " + user_name ", how good are you at volleyball?")))

if guess == SECRET: 
    print("Yes, you are correct, " + user_name + ", you do suck at this game?")
else:
    print("Do you think of yourself that poorly")
    if guess > SECRET:
         print("Homie, you need to try again.")
    else: 
        print("Well, I was going to give you a little credit.")


