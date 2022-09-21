"""Creating different functions."""

__author__ = "730545277"


def only_evens(evens: list[int]) -> list[int]:
    """Returns a list of even integers given a list of integers."""
    even_list: list[int] = list()
    index: int = 0
    while index < len(evens):
        if evens[index] % 2 == 0:
            even_list.append(evens[index])
        index += 1
    return even_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns all integers from first and second lists in one."""
    all_list: list[int] = list()
    index: int = 0
    while index < len(list_1):
        all_list.append(list_1[index])
        index += 1 
    
    index = 0
    while index < len(list_2):
        all_list.append(list_2[index])
        index += 1
    return all_list 


def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list of integers between given indexes."""
    subset_list: list[int] = ()
    index: int = start_index + 1
    
    if start_index > len(list):
        return []
    if len(list) == 0:
        return []
    if end_index < 0:
        return []
    while list[0] < start_index < len(list) and list[0] < end_index < len(list):
        subset_list.append(list[index])
        start_index += 1
    return subset_list
