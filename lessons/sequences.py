"""Notes and example of typle and range sequence types."""

# Declaring a type alias that "invents" the Point2D type
Point2D = tuple[float, float]

start_position: Point2D = (5.0, 10.0)
start_position = (start_position[0] + 6.0, start_position[1] + 1.0)
print(start_position)

# Examples of ranges 
# Range start: 0, Range end: 10, Range increment: 1 (the end of the range is not inclusive)
a_range: range = range(0, 10, 1)
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)

# An example of using the default parameter step 
# where the default step is 1 
another_range: range = range(0, 10)
for i in another_range:
    print(i)