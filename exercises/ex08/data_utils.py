"""Dictionary related utility functions."""

__author__ = "730545277"


from csv import DictReader 


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table (list of dicts)."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    return result 


def column_values(tablerows: list[dict[str, str]], columnname: str) -> list[str]:
    result: list[str] = list()
    for row in tablerows:
        result.append(row[columnname])
    return result 