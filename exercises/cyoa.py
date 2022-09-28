"""Creating a game called Tech Repair using Comp Questions."""

__author__ = "730545277"

playing_points: int = 0
player_name: str = ""

def repairing_in_progress(str) -> str:
    """Asking the players question to recieve tools and accessories."""
    CORRECT: str = "\unicode"
    INCORRECT: str = "\unicode"
    repair_progress: str = ""
    question_1: str = input("Answering question for: \.\What layer of a computing system's purpose is to make it easy for you as the user to start, control, and stop the processes on a computing system? Please type in the corresponding letter to the answer./ A: User Space Processes\ B: Shell\ C: OS Kernel\ D: Hardware\ ")
    while question_1 != "B":
        question_1 = input("Please pick a different answer: ")
    if question_1 == "B":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start fixing {FIXING_DEVICE}.\On to question 2.")

    question_2: str = input("Answering question for: \.\Stored Python programs typically end in what file extension suffix? Please type the corresponding letter to the answer.\A: .python \B: .python3\ C: .py\ D: .pyt\ ")
    while question_2 != "C":
        question_2 = input("Please pick a different answer: ")
    if question_2 == "C":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to continue fixing {FIXING_DEVICE}.\On to question 3.")

    question_3: input = str("Answering question for: \unicode.\Which of the following boolean expressions results in a value of True? Please type the corresponding letter to the answer.\A: 1 > 0\B: 1 != 2\C: 4 + 3 * 6 < 50\D: True == True\ ")
    while question_3 != "D":
        question_3 = input("Please pick a different answer: ")
    if question_3 == "D":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start continue {FIXING_DEVICE}.\On to question 4.")

    question_4: input = str("Answering question for: \unicode.\The condition of an if statement or while loop should always be a bool expression. Please type either True or False.\ ")
    while question_4 != "True":
        question_4 = input("Please pick a different answer: ")
    if question_4 == "True":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start continue {FIXING_DEVICE}.\On to question 5.")

    question_5: str = input("Answering question for: \unicode.\Evaluate the following expression: True and False or False and not False. Please type either True or False.\ ")
    while question_5 != "False":
        question_5 = input("Please pick a different answer: ")
    if question_5 == "False":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start fixing {FIXING_DEVICE}.\On to question 6.")

    question_6: str = input("Answering question for: \unicode.\Function definitions are found in which of the following ways... Please type the corresponding letter(s) to the answers(s).\For multiple correct answers, type letters without spaces.\A: Built-in functions are automatically available\B: Imported from libraries\C: Defined in the same python file / module\ ")
    while question_6 != "ABC":
        question_6 = input("Please pick a different answer: ")
    if question_6 == "ABC":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start fixing {FIXING_DEVICE}.\On to question 6.")

    question_7: str = input("Answering question for: \unicode.\What happens when a return statement is evaluated while tracing through a call to a function definition? Please type the corresponding letter(s) to the answer(s).\For multiple correct answers, type letters without spaces.\A: The expression following the return keyword is fully evaluated\B: The Return Value is recorded in the current frame on the stack\C: Jump back to the origination of the function call found in Return Address of frame and evaluate the function call expression to the return value in the stored in RV\D: Establish another new frame on the stack\ ")
    while question_7 != "ABC":
        question_7 = input("Please pick a different answer: ")
    if question_7 == "ABC":
        playing_points += 1
        print(f"You now have {playing_points}/10 points.")
        repair_progress += "\unicode"
        print("Correct! You now have (a) {repair_progress} to start fixing {FIXING_DEVICE}.\On to question 6.")

    question_8: str = input("Answering question for: \unicode.\"


def greet() -> None:
    """Introducing the player to the game."""
    global player_name
    player_name: str = input("What is your name?")
    print(f"Hello {player_name}, this is a game called Tech Repair.\ You currently are working as a tech repair person in the UNC shop.\ To fix the device and add accessories for the device to work, you must answer questions correctly relating to COMP 110 material.")
    print("You must answer a certain number of questions to find the right tools and accessories to fix and pair with the device in progress.\ Each question will show you the object you will be answering for.")
    FIXING_DEVICE: str = "\U0001F4BB\U0001FAAB"
    print(f"This is the device you will be fixing: {FIXING_DEVICE}.")
    ready_to_start: str = input("Please respond with YES if you are ready to play Tech Repair: ")
    repairing_in_progress(ready_to_start)   


def main() -> None:
    """Moving the player ownwards."""
    greet() 
        

if __name__ == "__main__":
    main()
