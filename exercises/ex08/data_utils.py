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
    i: int = 0 
    for column in columntable:
        result: list[dict[str, str]] = list()
        for row in column:
            if i < rownumber:
                result.append(row)
            i += 1
    return result


def select(columntable: dict[str, list[str]], columnname: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for items in columnname:
        result = columntable[items]
    return result



