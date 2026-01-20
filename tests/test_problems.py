"""
Test Suite for Problems
Tests problem definitions and their solutions.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problems import PathfindingProblem, MazeProblem, SchedulingProblem


class TestPathfindingProblem(unittest.TestCase):
    """Test cases for PathfindingProblem."""
    
    def setUp(self):
        self.problem = PathfindingProblem.create_city_map()
    
    def test_bfs_solution(self):
        result = self.problem.solve_bfs()
        self.assertTrue(result['found'])
        self.assertEqual(result['path'][0], 'London')
        self.assertEqual(result['path'][-1], 'Vienna')
    
    def test_dijkstra_solution(self):
        result = self.problem.solve_dijkstra()
        self.assertTrue(result['found'])
        self.assertIsInstance(result['cost'], (int, float))
        self.assertGreater(result['cost'], 0)
    
    def test_astar_solution(self):
        result = self.problem.solve_astar('euclidean')
        self.assertTrue(result['found'])
        self.assertIsInstance(result['cost'], (int, float))
    
    def test_algorithm_comparison(self):
        results = self.problem.compare_algorithms()
        
        # All algorithms should find a path
        for algo_name, result in results.items():
            self.assertTrue(result['found'], f"{algo_name} should find a path")
        
        # Dijkstra and A* should find same cost (optimal)
        dijkstra_cost = results['Dijkstra']['cost']
        astar_cost = results['A* (Euclidean)']['cost']
        self.assertEqual(dijkstra_cost, astar_cost)


class TestMazeProblem(unittest.TestCase):
    """Test cases for MazeProblem."""
    
    def setUp(self):
        self.maze = MazeProblem.create_sample_maze()
    
    def test_maze_creation(self):
        self.assertEqual(self.maze.rows, 9)
        self.assertEqual(self.maze.cols, 10)
    
    def test_bfs_solves_maze(self):
        result = self.maze.solve_bfs()
        self.assertTrue(result['found'])
        self.assertGreater(len(result['path']), 0)
    
    def test_astar_solves_maze(self):
        result = self.maze.solve_astar()
        self.assertTrue(result['found'])
        self.assertGreater(len(result['path']), 0)
    
    def test_visualization(self):
        result = self.maze.solve_bfs()
        if result['found']:
            visual = self.maze.visualize_solution(result['path'])
            self.assertIn('S', visual)  # Start marker
            self.assertIn('G', visual)  # Goal marker
            self.assertIn('*', visual)  # Path marker
    
    def test_algorithm_comparison(self):
        results = self.maze.compare_algorithms()
        
        # All algorithms should solve the maze
        for algo_name, result in results.items():
            self.assertTrue(result['found'], f"{algo_name} should solve the maze")
        
        # BFS and Dijkstra should find same length path (unweighted)
        bfs_length = len(results['BFS']['path'])
        dijkstra_length = len(results['Dijkstra']['path'])
        self.assertEqual(bfs_length, dijkstra_length)


class TestSchedulingProblem(unittest.TestCase):
    """Test cases for SchedulingProblem."""
    
    def setUp(self):
        self.problem = SchedulingProblem.create_software_project()
    
    def test_task_creation(self):
        self.assertEqual(len(self.problem.tasks), 8)
        self.assertIn('Requirements', self.problem.tasks)
        self.assertIn('Deployment', self.problem.tasks)
    
    def test_topological_sort(self):
        order = self.problem.topological_sort()
        self.assertIsNotNone(order)
        self.assertEqual(len(order), 8)
        
        # Requirements should come before Design
        req_idx = order.index('Requirements')
        design_idx = order.index('Design')
        self.assertLess(req_idx, design_idx)
        
        # Testing should come before Deployment
        test_idx = order.index('Testing')
        deploy_idx = order.index('Deployment')
        self.assertLess(test_idx, deploy_idx)
    
    def test_critical_path(self):
        result = self.problem.calculate_critical_path()
        
        self.assertIsNone(result['error'])
        self.assertIsNotNone(result['order'])
        self.assertIsNotNone(result['earliest_start'])
        self.assertIsNotNone(result['total_duration'])
        
        # Total duration should be positive
        self.assertGreater(result['total_duration'], 0)
        
        # Requirements should start at time 0
        self.assertEqual(result['earliest_start']['Requirements'], 0)
    
    def test_circular_dependency_detection(self):
        # Create a problem with circular dependency
        problem = SchedulingProblem()
        problem.add_task('A', 5)
        problem.add_task('B', 5)
        problem.add_task('C', 5)
        
        problem.add_dependency('B', 'A')
        problem.add_dependency('C', 'B')
        problem.add_dependency('A', 'C')  # Creates cycle
        
        order = problem.topological_sort()
        self.assertIsNone(order)  # Should detect cycle


if __name__ == '__main__':
    unittest.main()
