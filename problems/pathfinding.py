"""
Pathfinding Problem
General pathfinding on weighted graphs.
"""

from typing import Dict, List, Tuple
from data_structures import Graph
from algorithms import bfs_path, dfs_path, dijkstra, astar
from algorithms.astar import euclidean_distance, manhattan_distance


class PathfindingProblem:
    """
    Represents a general pathfinding problem on a graph.
    Can be solved with BFS, DFS, Dijkstra, or A*.
    """
    
    def __init__(self, graph: Graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.node_positions: Dict = {}  # For heuristic calculations
    
    def set_node_position(self, node_value, position: Tuple[float, float]):
        """Set the 2D position of a node for heuristic calculations."""
        self.node_positions[node_value] = position
    
    def solve_bfs(self) -> Dict:
        """Solve using Breadth-First Search."""
        from algorithms.bfs import breadth_first_search
        return breadth_first_search(self.graph, self.start, self.goal)
    
    def solve_dfs(self) -> Dict:
        """Solve using Depth-First Search."""
        from algorithms.dfs import depth_first_search
        return depth_first_search(self.graph, self.start, self.goal)
    
    def solve_dijkstra(self) -> Dict:
        """Solve using Dijkstra's algorithm."""
        return dijkstra(self.graph, self.start, self.goal)
    
    def solve_astar(self, heuristic_type: str = 'euclidean') -> Dict:
        """
        Solve using A* algorithm.
        
        Args:
            heuristic_type: 'euclidean', 'manhattan', or 'zero'
        """
        def heuristic(node1, node2):
            if node1 not in self.node_positions or node2 not in self.node_positions:
                return 0.0
            
            pos1 = self.node_positions[node1]
            pos2 = self.node_positions[node2]
            
            if heuristic_type == 'euclidean':
                return euclidean_distance(pos1, pos2)
            elif heuristic_type == 'manhattan':
                return manhattan_distance(pos1, pos2)
            else:
                return 0.0
        
        return astar(self.graph, self.start, self.goal, heuristic)
    
    def compare_algorithms(self) -> Dict:
        """
        Run all algorithms and compare their performance.
        
        Returns:
            Dictionary with results from each algorithm
        """
        results = {
            'BFS': self.solve_bfs(),
            'DFS': self.solve_dfs(),
            'Dijkstra': self.solve_dijkstra(),
        }
        
        # Only run A* if positions are set
        if self.node_positions:
            results['A* (Euclidean)'] = self.solve_astar('euclidean')
            results['A* (Manhattan)'] = self.solve_astar('manhattan')
        
        return results
    
    @staticmethod
    def create_city_map() -> 'PathfindingProblem':
        """
        Create a sample city map problem.
        
        Cities connected by roads with distances.
        """
        graph = Graph(directed=False)
        
        # Add edges (roads between cities)
        edges = [
            ('London', 'Paris', 344),
            ('London', 'Amsterdam', 358),
            ('Paris', 'Amsterdam', 431),
            ('Paris', 'Berlin', 878),
            ('Amsterdam', 'Berlin', 576),
            ('Berlin', 'Prague', 280),
            ('Paris', 'Madrid', 1054),
            ('Madrid', 'Barcelona', 504),
            ('Barcelona', 'Paris', 831),
            ('Berlin', 'Vienna', 524),
            ('Prague', 'Vienna', 251),
        ]
        
        for city1, city2, distance in edges:
            graph.add_edge(city1, city2, distance)
        
        problem = PathfindingProblem(graph, 'London', 'Vienna')
        
        # Set approximate positions (for heuristic)
        positions = {
            'London': (0, 51),
            'Paris': (2, 48),
            'Amsterdam': (4, 52),
            'Berlin': (13, 52),
            'Prague': (14, 50),
            'Vienna': (16, 48),
            'Madrid': (-3, 40),
            'Barcelona': (2, 41),
        }
        
        for city, pos in positions.items():
            problem.set_node_position(city, pos)
        
        return problem
