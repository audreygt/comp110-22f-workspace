"""Testing the dictionary functions."""

__author__ = "730545277"

from dictionaries import invert, favorite_color, count


def test_invert() -> None:
    """Testing test invert given correct list."""
    # Use case 
    dict_input: dict[str, str] = {"comp": "sci", "unc": "college"}
    assert invert(dict_input) == {"sci": "comp", "college": "unc"}


def test_invert_1() -> None:
    """Testing test invert given correct, longer list."""
    # Use case 
    dict_input: dict[str, str] = {"comp": "sci", "unc": "college", "audrey": "thomas", "ramsees": "jr"}
    assert invert(dict_input) == {"sci": "comp", "college": "unc", "thomas": "audrey", "jr": "ramsees"}


def test_invert_2() -> None:
    """Testing test invert given same keys."""
    # Edge case 
    dict_input: dict[str, str] = {"comp": "sci", "unc": "sci", "audrey": "thomas", "ramsees": "jr"}
    assert invert(dict_input) == KeyError("Duplicate keys present.")
    

def test_favorite_color() -> None:
    """Testing test favorite colors with correct dictionary."""
    # Use case
    color_input: dict[str, str] = {"audrey": "purple", "me": "blue", "you": "green", "yeet": "blue"}
    assert favorite_color(color_input) == "blue"


def test_favorite_color_2() -> None: 
    """Testing test favorite colors with all same colors."""
    # Use case
    color_input: dict[str, str] = {"audrey": "purple", "me": "purple", "you": "purple", "yeet": "purple"}
    assert favorite_color(color_input) == "purple"


def test_favorite_color_3() -> None: 
    """Testing test favorite colors with same number of colors."""
    # Use case 
    color_input: dict[str, str] = {"audrey": "purple", "me": "purple", "you": "green", "yeet": "green"}
    assert favorite_color(color_input) == "purple"
    

def test_count_1() -> None:
    """Testing presence of words using word count."""
    # Use case 
    word_input: list[str] = ["yes", "yes", "yes", "marshmallow", "halo", "lovely"]
    assert count(word_input) == {"yes": 3, "marshmallow" : 1, "halo": 1, "lovely": 1}


def test_count_2() -> None:
    """Testing count"""
    