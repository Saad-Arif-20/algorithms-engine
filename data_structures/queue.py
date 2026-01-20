"""
Custom Queue Implementation
FIFO (First In First Out) data structure.
"""

from typing import Optional, Any


class Queue:
    """
    Custom Queue implementation using a linked list approach.
    Time Complexity: O(1) for enqueue and dequeue operations.
    """
    
    class _Node:
        """Internal node class for the queue."""
        def __init__(self, value):
            self.value = value
            self.next: Optional['Queue._Node'] = None
    
    def __init__(self):
        self._front: Optional[Queue._Node] = None
        self._rear: Optional[Queue._Node] = None
        self._size = 0
    
    def enqueue(self, value: Any):
        """Add an element to the rear of the queue."""
        new_node = Queue._Node(value)
        
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        
        self._size += 1
    
    def dequeue(self) -> Any:
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        value = self._front.value
        self._front = self._front.next
        
        if self._front is None:
            self._rear = None
        
        self._size -= 1
        return value
    
    def peek(self) -> Any:
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._front.value
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._front is None
    
    def size(self) -> int:
        """Return the number of elements in the queue."""
        return self._size
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        elements = []
        current = self._front
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"Queue([{', '.join(elements)}])"
