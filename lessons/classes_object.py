"""Example of a class and object instantiation."""

class Pizza:
    # always name classes with capital letters
    # class is a keyword in python 
    """Models the idea of a Pizza."""
    # attribute definitons of Pizza
    size: str # = "small"
    toppings: int # = 0
    extra_cheese: bool = False


    def __init__(self, size: str, toppings: int):
        # automatically called when class is being mentioned
        """This is a constructor call for intializing attributes."""
        # This allows you to erase the attributes under class Pizza
        self.size = size 
        self.toppings = toppings 


# Self is a parameter that Python will establish 
    def pizza_price(self, tax: float) -> float:
        """Calculate the price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else: 
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total 


# def pizza_price(pizza: Pizza) -> float:
    # """Calculate the price of a pizza."""
    # total: float = 0.0
    # if pizza.size == "large":
        total += 10.0
    # else: 
        total += 8.0

    # total += pizza.toppings * 0.75

    # if pizza.extra_cheese:
        total += 1.0

    # return total 

#setting up the first pizza 
# a_pizza: Pizza = Pizza()
a_pizza: Pizza = Pizza("large", 3)
    # setting up the initial variables by calling pizza 
# pizza is now a valid class or variable in python 
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False 
# these are 3 variables combined or bundled into the class: Pizza
print(a_pizza)
# will result in object at a memory address 
print(a_pizza.size)
print(Pizza)
# will result in __main__ since Pizza is in this module
print(f"The price of the pizza: ${a_pizza.pizza_price(1.05)}.")
# changing from pizza_price since the function def in indented 
# this is a method call where variable is joined with function between .

another_pizza: Pizza = Pizza("small", 8)
another_pizza.extra_cheese = True 
print(another_pizza.size)
print(f"This is the price: ${another_pizza.pizza_price(1.05)}")