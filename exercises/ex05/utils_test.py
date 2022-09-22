"""Testing different functions."""

__author__ = "730545277"


from utils import only_evens
from utils import sub
from utils import concat 


def test_only_evens() -> None:
    """Testing only evens with a correct list."""
    # Use case
    evens: list[int] = [2, 3, 4, 5]
    assert only_evens(evens) == [2, 4]


def test_only_evens_empty_input() -> None:
    """Testing only evens with an empty inuput list."""
    # Edge case
    evens: list[int] = []
    assert only_evens(evens) == []


def test_only_evens_3() -> None:
    """Testing only_events using all odd list."""
    # Use 
    evens: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(evens) == []


def test_concat() -> None: 
    """Testing concat with right input lists."""
    # Use
    list_1: list[int] = [0, 1, 2]
    list_2: list[int] = [3, 4, 5]
    assert concat(list_1, list_2) == [0, 1, 2, 3, 4, 5]


def test_concat_2() -> None: 
    """Testing concat with an empty list."""
    # Use
    list_1: list[int] = []
    list_2: list[int] = [3, 4, 5]
    assert concat(list_1, list_2) == [3, 4, 5]


def test_concat_3() -> None:
    """Testing concat with both empty lists."""
    # Edge
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_sub() -> None:
    """Testing subs with indexes that fall in range."""
    # Use
    in_list: list[int] = [10, 20, 30, 40]
    start_index: int = 1
    end_index: int = 3
    assert sub(in_list, start_index, end_index) == [20, 30]


def test_sub_2() -> None: 
    """Testing subs with a start index equal to 0."""
    # Use
    in_list: list[int] = [10, 20, 30, 40]
    start_index: int = 0
    end_index: int = 4
    assert sub(in_list, start_index, end_index) == [10, 20, 30]


def test_sub_3() -> None: 
    """Tesing subs with an empty list."""
    # Edge 
    in_list: list[int] = [10, 20, 30, 40, 50]
    start_index: int = 0
    end_index: int = 7
    assert sub(in_list, start_index, end_index) == [10, 20, 30, 40]