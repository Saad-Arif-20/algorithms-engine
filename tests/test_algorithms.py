"""
Test Suite for Algorithms
Tests all pathfinding algorithms for correctness and performance.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures import Graph
from algorithms import breadth_first_search, depth_first_search, dijkstra, astar
from algorithms.astar import manhattan_distance


class TestBFS(unittest.TestCase):
    """Test cases for Breadth-First Search."""
    
    def setUp(self):
        """Create a simple graph for testing."""
        self.graph = Graph()
        edges = [
            ('A', 'B'), ('A', 'C'),
            ('B', 'D'), ('C', 'D'),
            ('D', 'E')
        ]
        for src, dst in edges:
            self.graph.add_edge(src, dst)
    
    def test_path_found(self):
        result = breadth_first_search(self.graph, 'A', 'E')
        self.assertTrue(result['found'])
        self.assertEqual(result['path'][0], 'A')
        self.assertEqual(result['path'][-1], 'E')
    
    def test_path_not_found(self):
        self.graph.add_node('Z')
        result = breadth_first_search(self.graph, 'A', 'Z')
        self.assertFalse(result['found'])
        self.assertEqual(result['path'], [])
    
    def test_shortest_path(self):
        # BFS should find shortest path in unweighted graph
        result = breadth_first_search(self.graph, 'A', 'D')
        self.assertTrue(result['found'])
        self.assertEqual(len(result['path']), 3)  # A -> B/C -> D


class TestDFS(unittest.TestCase):
    """Test cases for Depth-First Search."""
    
    def setUp(self):
        """Create a simple graph for testing."""
        self.graph = Graph()
        edges = [
            ('A', 'B'), ('A', 'C'),
            ('B', 'D'), ('C', 'E'),
            ('D', 'F'), ('E', 'F')
        ]
        for src, dst in edges:
            self.graph.add_edge(src, dst)
    
    def test_path_found(self):
        result = depth_first_search(self.graph, 'A', 'F')
        self.assertTrue(result['found'])
        self.assertEqual(result['path'][0], 'A')
        self.assertEqual(result['path'][-1], 'F')
    
    def test_path_not_found(self):
        self.graph.add_node('Z')
        result = depth_first_search(self.graph, 'A', 'Z')
        self.assertFalse(result['found'])


class TestDijkstra(unittest.TestCase):
    """Test cases for Dijkstra's Algorithm."""
    
    def setUp(self):
        """Create a weighted graph for testing."""
        self.graph = Graph()
        edges = [
            ('A', 'B', 4), ('A', 'C', 2),
            ('B', 'D', 5), ('C', 'D', 1),
            ('D', 'E', 3)
        ]
        for src, dst, weight in edges:
            self.graph.add_edge(src, dst, weight)
    
    def test_shortest_path(self):
        result = dijkstra(self.graph, 'A', 'E')
        self.assertTrue(result['found'])
        # Shortest path should be A -> C -> D -> E with cost 6
        self.assertEqual(result['cost'], 6.0)
        self.assertEqual(result['path'], ['A', 'C', 'D', 'E'])
    
    def test_direct_path_not_shortest(self):
        # Add a longer direct path
        self.graph.add_edge('A', 'E', 20)
        result = dijkstra(self.graph, 'A', 'E')
        # Should still choose the shorter multi-hop path
        self.assertEqual(result['cost'], 6.0)


class TestAStar(unittest.TestCase):
    """Test cases for A* Algorithm."""
    
    def setUp(self):
        """Create a grid-like graph with positions."""
        self.graph = Graph()
        
        # Create a 3x3 grid
        positions = {
            (0, 0): (0, 0), (0, 1): (0, 1), (0, 2): (0, 2),
            (1, 0): (1, 0), (1, 1): (1, 1), (1, 2): (1, 2),
            (2, 0): (2, 0), (2, 1): (2, 1), (2, 2): (2, 2)
        }
        
        self.positions = positions
        
        # Add horizontal and vertical connections
        for r in range(3):
            for c in range(3):
                if c < 2:
                    self.graph.add_edge((r, c), (r, c+1), 1.0)
                if r < 2:
                    self.graph.add_edge((r, c), (r+1, c), 1.0)
    
    def test_optimal_path(self):
        def heuristic(pos1, pos2):
            return manhattan_distance(pos1, pos2)
        
        result = astar(self.graph, (0, 0), (2, 2), heuristic)
        self.assertTrue(result['found'])
        # Manhattan distance from (0,0) to (2,2) is 4
        self.assertEqual(result['cost'], 4.0)
    
    def test_heuristic_efficiency(self):
        """A* should explore fewer nodes than Dijkstra with good heuristic."""
        def heuristic(pos1, pos2):
            return manhattan_distance(pos1, pos2)
        
        astar_result = astar(self.graph, (0, 0), (2, 2), heuristic)
        dijkstra_result = dijkstra(self.graph, (0, 0), (2, 2))
        
        # A* should explore same or fewer nodes
        self.assertLessEqual(astar_result['nodes_explored'], 
                           dijkstra_result['nodes_explored'])


class TestAlgorithmComparison(unittest.TestCase):
    """Compare different algorithms on the same problem."""
    
    def setUp(self):
        """Create a complex graph."""
        self.graph = Graph()
        edges = [
            ('A', 'B', 1), ('A', 'C', 4),
            ('B', 'C', 2), ('B', 'D', 5),
            ('C', 'D', 1), ('D', 'E', 3)
        ]
        for src, dst, weight in edges:
            self.graph.add_edge(src, dst, weight)
    
    def test_all_find_path(self):
        """All algorithms should find a path if one exists."""
        bfs_result = breadth_first_search(self.graph, 'A', 'E')
        dfs_result = depth_first_search(self.graph, 'A', 'E')
        dijkstra_result = dijkstra(self.graph, 'A', 'E')
        
        self.assertTrue(bfs_result['found'])
        self.assertTrue(dfs_result['found'])
        self.assertTrue(dijkstra_result['found'])
    
    def test_dijkstra_optimal(self):
        """Dijkstra should find the optimal path in weighted graphs."""
        result = dijkstra(self.graph, 'A', 'E')
        # Optimal path: A -> B -> C -> D -> E with cost 7
        self.assertEqual(result['cost'], 7.0)


if __name__ == '__main__':
    unittest.main()
