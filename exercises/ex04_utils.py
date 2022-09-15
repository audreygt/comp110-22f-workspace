"""Coding functions and using lists."""

__author__ = "730545277"

from ctypes.wintypes import LARGE_INTEGER


def all(sequence: list[int], check: int) -> bool:
    "Checking for all numbers in a sequence."
    index: int = 0
    checking: bool = True
    while index <= len(sequence) and checking is True:
        while sequence != list() and check == sequence[index]:
            index += 1
        return True
    while sequence == list() and check != sequence[index]:
        index += 1
        checking = False
        return False


def max(input: list[int]) -> int:
    """Checking for the largest number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list.")
    else:
        input.sort
        return (len(input) -1)


def is_equal(input: list[int], check: list[int]) -> bool:
    """Checking for equal input number sequence."""
    index = 0
    if input[index] == check[index]:
        index +=1 
        if input[index] == check[index]:
            index += 1
            if input[index] == check[index]:
                return True 
    else: 
        return False 