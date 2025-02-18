"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt 


__author__ = "730545277"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, location: Point) -> float:
        """Returning the distance between 2 cells."""
        x: float = self.x - location.x
        y: float = self.y - location.y
        distance: float = sqrt((x**2) + (y**2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign location attribute adding location with direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness = self.sickness + 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "dark violet"
        if self.is_immune():
            return "green" 
        return "gray"
        
    def contract_disease(self) -> None:
        """Changing cell from vulnerable to infected."""
        self.sickness = constants.INFECTED 

    def is_vulnerable(self) -> bool:
        """Returning true or false based on state."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returning true or false based on state."""
        state: bool
        if self.sickness >= constants.INFECTED:
            state = True 
        else: 
            state = False 
        return state 

    def contact_with(self, another: Cell) -> None:
        """Contracting dieases."""
        if self.is_vulnerable() and another.is_infected():
            self.contract_disease()
        if self.is_infected() and another.is_vulnerable():
            another.contract_disease()

    def immunize(self) -> None:
        """Becoming immune."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Becoming immune."""
        if self.sickness == constants.IMMUNE:
            return True 
        return False 


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, number: int, value: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if number >= cells or number <= 0:
            raise ValueError("Some cells must begin infected.")
        if value >= cells or value < 0:
            raise ValueError("Some cells must begin immune.")
        if number + value >= cells:
            raise ValueError("Some cells must start vulnerable.")
        else:
            for _ in range(cells):
                start_location: Point = self.random_location()
                start_direction: Point = self.random_direction(speed)
                cell: Cell = Cell(start_location, start_direction)
                self.population.append(cell)
        for i in range(0, number):
            self.population[i].contract_disease()
        for i in range(number, value + number):
            self.population[i].immunize()
        
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell) 
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None: 
        """Checking for distances."""
        for cell_number in range(0, len(self.population)):
            for cell_1 in range(cell_number + 1, len(self.population)):
                if self.population[cell_number].location.distance(self.population[cell_1].location) <= constants.CELL_RADIUS:
                    self.population[cell_number].contact_with(self.population[cell_1])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in range(0, len(self.population)):
            if self.population[i].is_infected(): 
                return False
        return True