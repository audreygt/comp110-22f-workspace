"""Creating a game called Tech Repair using Comp Questions."""

__author__ = "730545277"

from random import randint 
points: int
FIXING_DEVICE: str = "\U0001F4BB"
player: str = "name"
playing_turns: int = 0


def all_or_nothing(risky_points: int) -> int:
    """Allowing the player to risk all of their money by playing the lottery."""
    wizard_names: list[str] = ["Kris", "Kevin", "Ramsees"]
    wizard_index: int = randint(0, 2)
    gambling_computer: int = randint(0, 2)
    risky_points = int(risky_points)
    if gambling_computer == 0:
        risky_points -= risky_points 
        print(f"Oh no, {wizard_names[wizard_index]} made you lose all of your money and now you are still in debt to your UNC.")
    if gambling_computer == 1:
        risky_points += 10,0000
        print(f"Wow, {wizard_names[wizard_index]} thought the money would be helpful to pay off your UNC tuition debt.")
    if gambling_computer == 2:
        risky_points **= 10
        print(f"Amazing, {wizard_names[wizard_index]} wanted you to run up a check to pay off all of your UNC tuition.")
    points += risky_points 
    print(f"You have reached the end of the game, here are your total amount of money: {points}")


def customer_checking(points: int) -> int:
    """Random customers will now rate the compuer work done."""
    customer_names: list[str] = ["Kris\U0001F468", "Audrey\U0001F47D", "Aaron\U0001F468", "Shelly\U0001F469", "Karen\U0001F469"]
    customer_index: int = randint(0, 4)
    customer_rating: int = randint(1, 5)
    turn_number: int = 0 
    while customer_rating != 5 and turn_number < 3:
        if customer_rating == 1:
            points -= 10
            print(f"{customer_names[customer_index]}\U0001F92C rated your work on {FIXING_DEVICE} 1 star. You have lost all of your money and ended your business: \U0001F4B8{points}")
            print(f"Here is the customer's comment: \U0001F4AC Your work is complete #$%! but pass the {FIXING_DEVICE} to the next customer.")
        if customer_rating == 2:
            points //= .2
            print(f"{customer_names[customer_index]}\U0001FAE0 rated your work on {FIXING_DEVICE} 2 stars. They did not have a pleasent experience but did leave some money: \U0001F4B8{points}")
            print(f"Here is the customer's comment: \U0001F4AC You must have had a Dook education in computer science but pass the {FIXING_DEVICE} to the next customer.")
        if customer_rating == 3:
            points += 34
            print(f"{customer_names[customer_index]}\U0001F636 rated your work on {FIXING_DEVICE} 3 stars. They had a mediocre experience and left a surprise tip: \U0001F4B8{points}")
            print(f"Here is the customer's comment: \U0001F4AC You must have an NC Stink education in computer science but pass the {FIXING_DEVICE} to the next customer.")
        if customer_rating == 4:
            points *= 7
            print(f"{customer_names[customer_index]}\U0001F609 rated your work on {FIXING_DEVICE} 4 stars. They had a great experience and provided you with a fat tip: \U0001F4B8{points}")
            print(f"Here is the customer's comment: \U0001F4AC This worker must have attended the computer science program at UNC but may have slept in some of the lectures.\n Pass the {FIXING_DEVICE} to the next customer.")
        print(f"Maybe another customer may pick up this {FIXING_DEVICE} instead of the previous customer until 3 customers have rated your work.")
        input("Press enter.")
        points = points
        customer_index = randint(0, 4)
        customer_rating = randint(1,5)
        turn_number += 1
        if customer_rating == 5:
            points **= 3
            print(f"{customer_names[customer_index]}\U0001F911 rated your work on {FIXING_DEVICE} 5 stars. They had a terrific experience and wish you retirement: \U0001F4B8{points}")
            print(f"Here is the customer's comment: \U0001F4AC ""I can definitely tell you were taught by Kris Jordan in the comptuer science program at UNC-CH.\nTake my social security nunmber: 432-67-925""")
    global playing_turns
    playing_turns = 1
    main()
    return points 


def repairing_in_progress(points: int) -> str:
    """Asking the players question to recieve tools and accessories."""
    CORRECT: str = "\U00002705"
    INCORRECT: str = "\U0001F6AB"
    repair_progress: str = ""
    chances: int = 1
    question_1: str = input(f"Answering question for: \U0001FA9A.\nWhat layer of a computing system's purpose is to make it easy for you as the user to start, control, and stop the processes on a computing system? Please type in the corresponding letter to the answer.\nA: User Space Processes\nB: Shell\nC: OS Kernel\nD: Hardware\n")
    while question_1 != "B" and chances < 3:
        question_1 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_1 == "B":
        points += 1
        repair_progress += "\U0001FA9A"
        print(f"{CORRECT} Correct! You now have {points}/10 points and a {repair_progress}  to start fixing {FIXING_DEVICE}.\nOn to question 2.\n")
    chances = 0 

    question_2: str = input("Answering question for: \U0001F527.\nStored Python programs typically end in what file extension suffix? Please type the corresponding letter to the answer.\nA: .python\nB: .python3\nC: .py\nD: .pyt\n")
    while question_2 != "C" and chances < 3:
        question_2 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("The answer is wrong. Move onto the next question.")
    if question_2 == "C":
        points += 1
        repair_progress += "\U0001F527"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 3.\n")
    chances = 0 

    question_3: str = input(f"Answering question for: \U0001FA9B.\nWhich of the following boolean expressions results in a value of True? Please type the corresponding letter to the answer.\nA: 1 < 0\nB: 1 = 2\nC: 4 + 3 * 6 > 50\nD: True == True\n")
    while question_3 != "D" and chances < 3:
        question_3 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_3 == "D":
        points += 1
        repair_progress += "\U0001FA9B"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 4.\n")

    question_4: str = input(f"Answering question for: \U0001F529.\nThe condition of an if statement or while loop should always be a bool expression. Please type either True or False.\n")
    while question_4 != "True" and chances < 1:
        question_4 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_4 == "True":
        points += 1
        repair_progress += "\U0001F529"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 5.\n")
    chances = 0 

    question_5: str = input(f"Answering question for: \U00002699.\nEvaluate the following expression: True and False or False and not False. Please type either True or False.\n")
    while question_5 != "False" and chances < 1:
        question_5 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_5 == "False":
        points += 1
        repair_progress += "\U00002699"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 6.\n")
    chances = 0 

    question_6: str = input(f"Answering question for: \U0001F9AF .\nFunction definitions are found in which of the following ways... Please type the corresponding letter(s) to the answers(s).\nFor multiple correct answers, type letters without spaces.\nA: Built-in functions are automatically available\nB: Imported from libraries\nC: Defined in the same python file / module\n")
    while question_6 != "ABC" and chances < 3:
        question_6 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_6 == "ABC":
        points += 1
        repair_progress += "\U0001F9AF"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 7.\n")
    chances = 0 

    question_7: str = input(f"Answering question for: \U0001F50B.\nWhat happens when a return statement is evaluated while tracing through a call to a function definition? Please type the corresponding letter(s) to the answer(s).\nFor multiple correct answers, type letters without spaces.\nA: The expression following the return keyword is fully evaluated\nB: The Return Value is recorded in the current frame on the stack\nC: Jump back to the origination of the function call found in Return Address of frame and evaluate the function call expression to the return value in the stored in RV\nD: Establish another new frame on the stack\n")
    while question_7 != "ABC" and chances < 3:
        question_7 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_7 == "ABC":
        points += 1
        repair_progress += "\U0001F50B"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 8.\n")
    chances = 0 

    question_8: str = input(f"Answering question for: \U0001F3A7.\nIn what scenario is __name__ assigned ""__main__""? Please type the corresponding letter to the answer.\nA: When a Python module is beign run as a program such as python -m lessons.imports/\nB: When a Python module is being imported into another module\n")
    while question_8 != "A" and chances < 3:
        question_8 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_8 == "A":
        points += 1
        repair_progress += "\U0001F3A7"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 9.\n")
    chances = 0 

    question_9: str = input(f"Answering question for: \U0001F50C.\nWhich of the following names is likely to be a named constant? Please type the corresponding letter to the answer.\nA: tech_repair\nB: TechRepair\nC: techRepair\nD: TECH_REPAIR\n")
    while question_9 != "D" and chances < 3:
        question_9 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_9 == "D":
        points += 1
        repair_progress += "\U0001F50C"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress} to continue fixing {FIXING_DEVICE}.\nOn to question 10.\n")
    chances = 0 

    question_10: str = input("Answering question for \U0001F5B1.\nFor any task, a for..in loop can achieve, writing a while loop to achieve the same result will typically result in less code for you to write. Please either type True orFalse.\n")
    while question_10 != "False" and chances < 1:
        question_10 = input(f"{INCORRECT} Please pick a different answer: ")
        chances += 1
    print("This answer is wrong, move onto the next question.")
    if question_10 == "False":
        points += 1
        repair_progress += "\U0001F5B1"
        print(f"{CORRECT} Correct! You now have {points}/10 points and {repair_progress}  to finish fixing {FIXING_DEVICE}.")
    chances = 0 

    print(f"The {FIXING_DEVICE} is now completed. The customer\U0001F468\U0001F469 will now come back to recieve their laptop and rate your work.\n{player}, please be prepapred to serve the {FIXING_DEVICE} to the customer.\nLet's move onto the next step, your shift is almost over.\n")
    input("Press enter.")
    global points
    customer_checking(points)
    return points


def greet() -> None:
    """Introducing the player to the game."""
    global player
    player = input("What is your name? ")
    print(f"Hello {player}, this is a game called Tech Repair\U000000A9\U000000AE\U00002122.\nYou currently are working as a tech repair person in the UNC shop.\nYour goal is to make enough money to pay off all of your UNC tuition.\nTo fix the device and add accessories for the device to work, you must answer questions correctly relating to COMP 110 material.")
    input("Press enter.\n")
    print("You must answer a certain number of questions to find the right tools and accessories to fix and pair with the device in progress.\nEach question will show you the object you will be answering for.")
    input("Press enter.\n")
    print(f"Near the end of your work shift, the device will be rated by the customers in which your points will then turn into your paycheck for the end of the day.")
    input("Press enter.\n")
    print(f"This is the device you will be fixing: {FIXING_DEVICE}\U0001FAAB , a broken computer.")
    input("Press enter when you are ready to start.\n")


def main() -> None:
    """Moving the player ownwards."""
    global playing_turns
    if playing_turns == 0:
        global points
        points = 0
        greet() 
        global points
        repairing_in_progress(points)
        global points
        customer_checking(points)
        playing_turns += 1
    else: 
        print(f"So far, here are your points: {points}")
        game_choice: str = input("Would you like to quit the game, risk your money, or redo the game?\nPlease type 1 to quit, 2 to continue, 3 to redo the game.\nChoosing to risk you money allows the computer to determine what the machine should do based on the amount of money you have provided.\n")
        if game_choice == "1":
            print(f"Thank you for playing, here are your total number of points: {points}")
        if game_choice == "2":
            print("Now that you have earned your money based on you work, you now will go gamnle your money.")
            risky_points: int = input("How many of your points gathered so far would you like to risk?\n")
            all_or_nothing(risky_points)
        if game_choice == "3":
            global points
            points = 0
            repairing_in_progress(points)

        
if __name__ == "__main__":
    main()
