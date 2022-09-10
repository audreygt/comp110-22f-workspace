"""Examples of using lists in a simple 'game'."""

from random import randint

rolls: list[int] = list() # setting up an empty list
while len(rolls) == 0 or rolls[len(rolls) -1] != 1:
    rolls.append(randint(1,6)) # adding items to the list
print(rolls)

#remove an items from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of numbers rolled by rolls 
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1
print(f"Total score: {sum}")


# rolls: list[int] = list() # setting up an empty list 
# rolls.append(1) # telling rolls to add number to list
# rolls.append(3)
# rolls.append(randint(1, 6))
# print(rolls)

# # to access an individual item in the list 
# print(rolls[0])
# print(rolls[1])

# print(rolls[len(rolls) -1])