"""Examples of "vectorized" operations via magic methods."""

from __future__ import annotations 
from typing import Union 

class StrArray: 
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items 

    def __repr__(self) -> str: 
        return f"StrArray({self.items})"

    def __add__(self, right: Union[str, StrArray]) -> StrArray: 
        result: StrArray = StrArray([])
        if isinstance(right, str):
            for item in self.items:
                item += right 
                result.items.append(item)
            else: 
                for i in range(0, len(self.items)):
                    result.items.append(self.items[i] + right[i])
        return result 

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
# result:     StrArray(['Armando', 'Pete', 'Leaky'])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + " " + b)