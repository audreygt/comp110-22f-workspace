"""Dictionary related utility functions."""

__author__ = "730545277"


from csv import DictReader 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table (list of dicts)."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(tablerows: list[dict[str, str]], columnname: str) -> list[str]:
    """Creating a list of values from columns."""
    result: list[str] = list()
    for row in tablerows:
        result.append(row[columnname])
    return result 


def columnar(rowtable: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforming table of rows into table of columns."""
    result: dict[str, list[str]] = {}
    starting_row: dict[str, str] = rowtable[0]
    for column in starting_row:
        result[column] = column_values(rowtable, column)
    return result 


def head(columntable: dict[str, list[str]], rownumber: int) -> dict[str, list[str]]:
    result: dict[str, list[int]] = {} 
    for column in columntable: 
        new_list: list[str] = list()
        for item in range(rownumber):
            new_list.append(columntable[column][item])
            result[column] = new_list
    return result


def count(word_input: list[str]) -> dict[str, int]:
    """Tracking the presence of words in a list."""
    word_dict: dict[str, int] = {}
    index: int = 0
    for words in word_input:
        if word_input[index] in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
        index += 1
    return word_dict 