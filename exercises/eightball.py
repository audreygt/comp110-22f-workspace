from random import randint

question: str = input("Ask a yes/no question...")
response: int = randint(0, 2)

if response == 0:
    print("Yes, deifnitely.")
elif response == 1: 
    print("Ask again later.")
elif response == 2:
    print("Crying in the club.")
else: 
    print("My sources says no.")