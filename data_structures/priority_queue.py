"""
Custom Priority Queue Implementation
Min-heap based priority queue for efficient priority-based operations.
"""

from typing import Any, Tuple, List


class PriorityQueue:
    """
    Custom Priority Queue implementation using a binary min-heap.
    Time Complexity: O(log n) for insert and extract_min operations.
    """
    
    def __init__(self):
        self._heap: List[Tuple[float, Any]] = []  # (priority, value)
        self._size = 0
    
    def insert(self, value: Any, priority: float):
        """Insert an element with a given priority."""
        self._heap.append((priority, value))
        self._size += 1
        self._heapify_up(self._size - 1)
    
    def extract_min(self) -> Tuple[float, Any]:
        """Remove and return the element with minimum priority."""
        if self.is_empty():
            raise IndexError("extract_min from empty priority queue")
        
        min_item = self._heap[0]
        
        # Move last element to root and heapify down
        self._heap[0] = self._heap[self._size - 1]
        self._heap.pop()
        self._size -= 1
        
        if not self.is_empty():
            self._heapify_down(0)
        
        return min_item
    
    def peek_min(self) -> Tuple[float, Any]:
        """Return the element with minimum priority without removing it."""
        if self.is_empty():
            raise IndexError("peek_min from empty priority queue")
        return self._heap[0]
    
    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return self._size == 0
    
    def size(self) -> int:
        """Return the number of elements in the priority queue."""
        return self._size
    
    def _heapify_up(self, index: int):
        """Restore heap property by moving element up."""
        parent = (index - 1) // 2
        
        if index > 0 and self._heap[index][0] < self._heap[parent][0]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            self._heapify_up(parent)
    
    def _heapify_down(self, index: int):
        """Restore heap property by moving element down."""
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < self._size and self._heap[left][0] < self._heap[smallest][0]:
            smallest = left
        
        if right < self._size and self._heap[right][0] < self._heap[smallest][0]:
            smallest = right
        
        if smallest != index:
            self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
            self._heapify_down(smallest)
    
    def __len__(self):
        return self._size
    
    def __repr__(self):
        return f"PriorityQueue({self._heap})"
