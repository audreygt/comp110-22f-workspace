"""Dictionary related utility functions."""

__author__ = "730545277"


from csv import DictReader 


def read_csv_rows(filename:str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table (list of dicts)."""
    result: list[dict[str, str]] = []