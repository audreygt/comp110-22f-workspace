"""Coding functions and using lists."""

__author__ = "730545277"


def all(sequence: list[int], check: int) -> bool:
    """Checking for all numbers in a sequence."""
    index: int = 0
    while index < len(sequence):
        if len(sequence) != 0 and check == sequence[index]:
            index += 1
        else:
            return False
    return True 


def max(input: list[int]) -> int:
    """Checking for the largest number."""
    maximum: int = 0
    index = 0 
    if len(input) == 0:
        raise ValueError("max() arg is an empty list.")
    else:
        while index < len(input):
            if abs(input[index]) > maximum:
                maximum = input[index]
            index += 1
        return maximum


def is_equal(input: list[int], check: list[int]) -> bool:
    """Checking for equal input number sequence."""
    index = 0
    while index < len(input): 
        if input[index] == check[index] and len(input) == len(check):
            index += 1 
        else: 
            return False 
    return True