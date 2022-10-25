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
    """Listing a few of the column names."""
    result: dict[str, list[str]] = {} 
    for column in columntable: 
        new_list: list[str] = []
        for item in range(0, rownumber):
            if len(new_list) < len(columntable[column]):
                new_list.append(columntable[column][item])
        result[column] = new_list
    return result


def select(columntable: dict[str, list[str]], list_1: list[str]) -> dict[str, list[str]]:
    """Producing a dictionary with keys matching list of strings."""
    result: dict[str, list[str]] = {}
    for columns in list_1:
        if columns in columntable:
            result[columns] = columntable[columns]
    return result 


def concat(columntable_1: dict[str, list[str]], columntable_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Producing a new dictionary consisting of both given dictionaries."""
    result: dict[str, list[str]] = {}
    for columns in columntable_1:
        result[columns] = columntable_1[columns]
    for columns in columntable_2:
        if columntable_2[columns] == result[columns]:
            result[columns] = columntable_2[columns]
    return result 


def count(list_1: list[str]) -> dict[str, int]:
    """Tracking the presence of words in a list."""
    result: dict[str, int] = {}
    index: int = 0
    for words in list_1:
        if list_1[index] in result:
            result[words] += 1
        else:
            result[words] = 1
        index += 1
    return result