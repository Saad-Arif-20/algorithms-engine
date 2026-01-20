"""
Test Suite for Data Structures
Tests all custom data structures for correctness.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures import Graph, Queue, Stack, PriorityQueue, BinaryTree


class TestGraph(unittest.TestCase):
    """Test cases for Graph data structure."""
    
    def test_add_node(self):
        graph = Graph()
        graph.add_node('A')
        self.assertEqual(len(graph), 1)
        self.assertIsNotNone(graph.get_node('A'))
    
    def test_add_edge_undirected(self):
        graph = Graph(directed=False)
        graph.add_edge('A', 'B', 5.0)
        
        self.assertEqual(graph.get_edge_weight('A', 'B'), 5.0)
        self.assertEqual(graph.get_edge_weight('B', 'A'), 5.0)
    
    def test_add_edge_directed(self):
        graph = Graph(directed=True)
        graph.add_edge('A', 'B', 5.0)
        
        self.assertEqual(graph.get_edge_weight('A', 'B'), 5.0)
        self.assertEqual(graph.get_edge_weight('B', 'A'), float('inf'))
    
    def test_get_neighbors(self):
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        
        neighbors = graph.get_neighbors('A')
        neighbor_values = [n.value for n in neighbors]
        
        self.assertEqual(len(neighbors), 2)
        self.assertIn('B', neighbor_values)
        self.assertIn('C', neighbor_values)


class TestQueue(unittest.TestCase):
    """Test cases for Queue data structure."""
    
    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
    
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        
        queue.dequeue()
        self.assertTrue(queue.is_empty())
    
    def test_peek(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 2)  # Peek doesn't remove
    
    def test_size(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)
        
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)


class TestStack(unittest.TestCase):
    """Test cases for Stack data structure."""
    
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
    
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        
        stack.push(1)
        self.assertFalse(stack.is_empty())
        
        stack.pop()
        self.assertTrue(stack.is_empty())
    
    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(len(stack), 2)  # Peek doesn't remove


class TestPriorityQueue(unittest.TestCase):
    """Test cases for Priority Queue data structure."""
    
    def test_insert_extract_min(self):
        pq = PriorityQueue()
        pq.insert('task1', 5)
        pq.insert('task2', 2)
        pq.insert('task3', 8)
        
        priority, value = pq.extract_min()
        self.assertEqual(priority, 2)
        self.assertEqual(value, 'task2')
        
        priority, value = pq.extract_min()
        self.assertEqual(priority, 5)
    
    def test_heap_property(self):
        pq = PriorityQueue()
        values = [10, 5, 15, 3, 8, 20, 1]
        
        for i, val in enumerate(values):
            pq.insert(f'item{i}', val)
        
        # Extract all and verify they come out in sorted order
        extracted = []
        while not pq.is_empty():
            priority, _ = pq.extract_min()
            extracted.append(priority)
        
        self.assertEqual(extracted, sorted(values))


class TestBinaryTree(unittest.TestCase):
    """Test cases for Binary Tree data structure."""
    
    def test_insert(self):
        tree = BinaryTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)
        
        self.assertEqual(tree.size(), 3)
    
    def test_traversals(self):
        tree = BinaryTree()
        for val in [1, 2, 3, 4, 5]:
            tree.insert(val)
        
        # Test that traversals return correct number of elements
        self.assertEqual(len(tree.inorder_traversal()), 5)
        self.assertEqual(len(tree.preorder_traversal()), 5)
        self.assertEqual(len(tree.postorder_traversal()), 5)


if __name__ == '__main__':
    unittest.main()
