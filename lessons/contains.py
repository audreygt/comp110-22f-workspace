"""An example of a list utility algorithm."""

#function with 2 parameters, needle is what we are searching for, haystack is what we are searching in.
def contains(needle: str = input, haystack: list[str] = list()) -> bool:
    index: int = 0
    while index <= len(haystack):
        if needle == haystack[index]:
            return True 
        else: 
            index += 1 
            return False

