class Student:
    email: str 

    def __init__(self, email):
        self.email = email 

class Gradebook:
    grades: dict[Student, float]

    def __init__(self):
        self.grades = {}

    def add_student(self, student: Student, grade: float) -> None:
        self.grades[student] = grade 
    
    def outreach(self) -> list[str]:
        result: list[str] = []
        for student in self.grades:
            if self.grades[student] < 75.0:
                result.append(student.email)
        return result 

class ChristmasTreeFarm:
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        self.plots.append(initial_planting)
        for plots in range(plots):
            self.plots.append(0)

    def plant(self, integer: int):
        self.plots[integer] = 1

    def growth(self):
        for i in range(len(self.plots) - 1):
            if self.plots[i] > 0:
                self.plots[i] += 1

    def harvest(self, replant: bool) -> int:
        harvested: int = 0 
        for i in range(len(self.plots) - 1): 
            if self.plots[i] >= 5: 
                if  replant:
                    self.plots[i] = 1
                elif not replant:
                    self.plots[i] = 0
                harvested += 1
        return harvested

    def __add__(self, another: ChristmasTreeFarm) -> ChristmasTreeFarm:
        new_farm: int = 0 
        for i in self.plots: 
            if i > 0:
                new_farm += 1
        for i in another:
            if i > 0:
                new_farm += 1
        return ChristmasTreeFarm(new_farm)

class Course: 
    name: str
    level: int 
    prerequisites: list[str]

    def __init__(self, names, levels, prerequisites):
        self.name = names
        self.level = levels
        self.prerequistes = prerequisites 

    def find_courses(list_courses: list[Courses], prereq: list[str]) -> list[str]: 
        advanced_classes: list[str] = []
        for i in list_courses:
            if i.level >= 400: 
                for requirements in i.prerequisites:
                    if requirements == prereq:
                        advanced_classes.append(i.name)
        return advanced_classes 

    def is_valid_course(self, prereq: list[str]) -> bool:
        if self.level >= 400 and self.prerequisites == prereq:
            return True 
        return False 
            

