"""Coding functions and using lists."""

__author__ = "730545277"

from ctypes.wintypes import LARGE_INTEGER
from random import randint 


def all(input: list[int], check: int) -> bool:
    "Checking for all numbers in a sequence."
    if input == list() or check != input:
        return False
    else: 
        return True


def max(input: list[int]) -> int:
    """Checking for the largest number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list.")
    if len(input) <= 3:
        return LARGE_INTEGER


def is_equal(input: list[int], check: list[int]) -> bool:
    """Checking for equal input number sequence."""
    if input == check:
        return True 
    else: 
        return False 
