"""Practicing with recursions."""

from __future__ import annotations

from typing import Union, Optional

class Node:
    data: int
    next: Union[Node, None]

    #def __init__(self, data: int, next: Union[Node, None]):
    def __init__(self, data: int, next: Optional[Node]):
        self.data = data 
        self.next = next 

    def __str__(self) -> str:
        if self.next == None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"

# Simple way to code for recursion
# head: Node = Node(1, None)
# tail: Node = Node(2, None)
# head.next = tail 


# A way to code for procedural recursion 
# def sum(node: Node) -> int:
    # if node.next == None:
        # return node.data 
    # else:
        # return node.data + sum(node.next)
    
# A more concise way to code 
def sum(node: Optional[Node]) -> int:
    if node == None:
        return 0
    else:
        return node.data + sum(node.next)  

# def count(node: Node, current: int = 0) -> int:
    if node.next == None:
        return current + 1
    else: 
        return count(node.next, current + 1)

def count(node: Optional[Node], current: int = 0) -> int:
    if node == None:
        return current 
    else: 
        return count(node.next, current + 1)

# An easier way to code for structural recursion 
head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
