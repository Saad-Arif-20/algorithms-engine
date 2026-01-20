"""
Custom Stack Implementation
LIFO (Last In First Out) data structure.
"""

from typing import Optional, Any


class Stack:
    """
    Custom Stack implementation using a linked list approach.
    Time Complexity: O(1) for push and pop operations.
    """
    
    class _Node:
        """Internal node class for the stack."""
        def __init__(self, value):
            self.value = value
            self.next: Optional['Stack._Node'] = None
    
    def __init__(self):
        self._top: Optional[Stack._Node] = None
        self._size = 0
    
    def push(self, value: Any):
        """Add an element to the top of the stack."""
        new_node = Stack._Node(value)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self) -> Any:
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value
    
    def peek(self) -> Any:
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.value
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self._top is None
    
    def size(self) -> int:
        """Return the number of elements in the stack."""
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        elements = []
        current = self._top
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"Stack([{', '.join(elements)}])"
