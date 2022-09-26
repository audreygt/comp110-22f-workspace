"""An example for in syntax."""

names: list[str] = ["Shelly", "Audrey", "Aaron"]

# example of interating through names uning a whie loop 
print("while output result")
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# example of interating through names using a for in loop 
print("for in output result")
for name in names:
    print(name)
