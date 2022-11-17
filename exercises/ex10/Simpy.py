"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730545277"


class Simpy:
    """Simping for simpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructing a list of values."""
        self.values = values 

    def __repr__(self) -> str:
        """Constructing a string."""
        return f"Simpy({self.values})"

    def fill(self, floats: float, number: int) -> None: 
        """Filling in the values under the limit of number."""
        self.values = []
        i: int = 0 
        while i < number:
            self.values.append(floats)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        """Implementing numbers throuhg a range skipping by step."""
        ending: float = stop - step
        while abs(start) <= abs(ending):
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Sums up all values in the Simpy list."""
        total: float = sum(self.values)
        return total 

    def __add__(self, choice: Union[Simpy, float]) -> Simpy:
        """Adding values together."""
        result: list[float] = []
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                result.append(self.values[i] + choice.values[i])
            
        if isinstance(choice, float):
            for i in range(len(self.values)):
                result.append(self.values[i] + choice)
        return Simpy(result)

    def __pow__(self, choice: Union[Simpy, float]) -> Simpy:
        """Using exponents and increasing values."""
        result: list[float] = []
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                result.append(self.values[i] ** choice.values[i])
            
        if isinstance(choice, float):
            for i in range(len(self.values)):
                result.append(self.values[i] ** choice)
        return Simpy(result)

    def __eq__(self, choice: Union[Simpy, float]) -> list[bool]:
        """Checking for anything that equals."""
        result: list[bool] = []
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                if self.values[i] == choice.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        if isinstance(choice, float):
            for i in range(len(self.values)):
                if self.values[i] == choice:
                    result.append(True)
                else:
                    result.append(False)
        return result 

    def __gt__(self, choice: Union[Simpy, float]) -> list[bool]:
        """Returning bools based on conditions."""
        result: list[bool] = []
        if isinstance(choice, Simpy):
            for i in range(len(self.values)):
                if self.values[i] > choice.values[i]:
                    result.append(True)
                elif self.values[i] < choice.values[i]:
                    result.append(False)
        if isinstance(choice, float):
            for i in range(len(self.values)):
                if self.values[i] > choice:
                    result.append(True)
                else:
                    result.append(False)
        return result 

    def __getitem__(self, choice: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Pulling items out using bools."""
        if isinstance(choice, int):
            return (self.values[choice])
            
        else: 
            result: list[float] = []
            for i in range(len(choice)):
                if choice[i] is True:
                    result.append(self.values[i])
            return Simpy(result)    