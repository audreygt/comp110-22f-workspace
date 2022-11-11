"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        self.values = values 

    def __repr__(self) -> str:
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
        stop -= step
        floats: float = start
        while floats <= stop: 
            self.values.append(floats + step)

    def sum(self) -> float:
        """Sums up all values in the Simpy list."""
        total: float = sum(self.values)
        return total 

    def __add__(self, choice: Union[Simpy, float]) -> Simpy:
        result: Simpy = Simpy([])
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                result += (self.values[i] + choice.values[i])
            
        if isinstance(choice, float):
            for i in range(len(self.values)):
                result += (self.values[i] + choice)
        return result

    def __pow__(self, choice: Union[Simpy, float]) -> Simpy:
        result: Simpy = Simpy([])
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                result += (self.values[i] ** choice.values[i])
            
        if isinstance(choice, float):
            for i in range(len(self.values)):
                result += (self.values[i] ** choice)
        return result

    def __eq__(self, choice: Union[Simpy, float]) -> list[bool]:
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
        result: list[bool] = []
        if isinstance(choice, Simpy):
            assert len(self.values) == len(choice.values)
            for i in range(len(self.values)):
                if self.values[i] > choice.values[i]:
                    result.append(True)
                else: 
                    result.append(False)
        if isinstance(choice, float):
            for i in range(len(self.values)):
                if self.values[i] > choice:
                    result.append(True)
                else:
                    result.append(False)
        return result 

    def __getititem__(self, choice: Union[int, list[bool]]) -> float:
        result: float = 0.0
        if isinstance(choice, int):
            if choice < len(self.values):
                result = self.values[choice]
        if isinstance(choice, list[bool]):
            for i in choice:
                if self.values[i] == choice[True]:
                    result += (self.values[i])
        return result 
        
      
        





            
    




        