"""Testing different functions."""

__author__ = "730545277"


from utils import only_evens
from utils import sub
from utils import concat 


def test_only_evens() -> None:
    """Testing only evens."""
    evens: list[int] = list[2, 3, 4, 5]
    assert only_evens(evens) == [2, 4]


def test_sub() -> None:
    """Testing subs."""
    list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert start_index <= end_index
    assert sub(list, start_index, end_index) == [20, 30]


def test_concat() -> None: 
    """Testing concat."""
    list_1: list[int] = [0, 1, 2]
    list_2: list[int] = [3, 4, 5]
    assert concat(list_1, list_2) == [0, 1, 2, 3, 4, 5]