"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: str) -> str: 
    """To return a delightful greeting."""
    greeting: str = "Hello, " + name
    return greeting 

print(hello("Sally"))

# write a function with no arguments 
# writing a default value for parameters 
# make sure default parameters are placed last 
# optional paramters should be listed after required parameters 
def hello1(name: str = "World") -> str: 
    """To return a delightful greeting."""
    greeting: str = "Hello, " + name
    return greeting 

print(hello1())

def hello3(name: Union[str, int, float] = "World") -> str: 
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name 
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else: 
        greeting += "Alien Life from Sector " + str(name)
    return greeting 
print("This is the beginning of the hello3 function.")
print(hello3("Sally"))
print(hello3())
print(hello3(110))
print(hello3(3.14))



