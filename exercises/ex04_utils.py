"""Coding functions and using lists."""

__author__ = "730545277"

from random import randint 

def all(sequence: list(), int: int) -> bool:
    "Checking for all numbers in a sequence."
    number_set: list[int] = list()
    check_number: int = randint(1,10)
    playing: bool = True
    while len(number_set) <= 3 and playing == True:
        number_set.append(randint(1,10))
    if 