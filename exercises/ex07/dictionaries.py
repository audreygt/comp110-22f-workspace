"""EX07 - practiing with dictionaries."""

__author__ = "730545277"


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    """Inverting a dictionary given dictionary."""
    new_dict: dict[str, str] = {}
    for items in dict_input:
        if dict_input[items] in new_dict:
            raise KeyError("Duplicate keys present.")
        new_dict[dict_input[items]] = items
    return new_dict


def favorite_color(color_input: dict[str, str]) -> str:
    """Printing out most common color."""
    common_color: str = ""
    color_amount: dict[str, int] = {}
    for names in color_input:
        if color_input[names] in color_amount:
            color_amount[color_input[names]] += 1
        else:
            color_amount[color_input[names]] = 1
    color_max: int = 0
    for color in color_amount:
        if color_amount[color] > color_max:
            color_max = color_amount[color]
            common_color = color 
    return common_color 


def count(word_input: list[str]) -> dict[str, int]:
    """Tracking the presence of words in a list."""
    word_dict: dict[str, int] = {}
    index: int = 0
    for words in word_input:
        if word_input[0] in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
        index += 1
    return word_dict 