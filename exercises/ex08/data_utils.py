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


