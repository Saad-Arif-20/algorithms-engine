"""
Maze Problem
Pathfinding in a 2D grid maze.
"""

from typing import List, Tuple, Dict
from data_structures import Graph
from algorithms import bfs_path, dfs_path, dijkstra, astar
from algorithms.astar import manhattan_distance


class MazeProblem:
    """
    Represents a maze as a 2D grid.
    '#' represents walls, '.' represents open paths.
    """
    
    def __init__(self, maze: List[List[str]], start: Tuple[int, int], goal: Tuple[int, int]):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if maze else 0
        self.start = start
        self.goal = goal
        self.graph = self._build_graph()
    
    def _build_graph(self) -> Graph:
        """Convert the maze into a graph representation."""
        graph = Graph(directed=False)
        
        # Add edges for adjacent walkable cells
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == '#':
                    continue
                
                current = (r, c)
                
                # Check all 4 directions (up, down, left, right)
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.maze[nr][nc] != '#':
                            neighbor = (nr, nc)
                            graph.add_edge(current, neighbor, 1.0)
        
        return graph
    
    def solve_bfs(self) -> Dict:
        """Solve maze using BFS."""
        from algorithms.bfs import breadth_first_search
        return breadth_first_search(self.graph, self.start, self.goal)
    
    def solve_dfs(self) -> Dict:
        """Solve maze using DFS."""
        from algorithms.dfs import depth_first_search
        return depth_first_search(self.graph, self.start, self.goal)
    
    def solve_dijkstra(self) -> Dict:
        """Solve maze using Dijkstra's algorithm."""
        return dijkstra(self.graph, self.start, self.goal)
    
    def solve_astar(self) -> Dict:
        """Solve maze using A* with Manhattan distance heuristic."""
        def heuristic(pos1, pos2):
            return manhattan_distance(pos1, pos2)
        
        return astar(self.graph, self.start, self.goal, heuristic)
    
    def visualize_solution(self, path: List[Tuple[int, int]]) -> str:
        """
        Visualize the maze with the solution path.
        
        Args:
            path: List of (row, col) positions representing the path
        
        Returns:
            String representation of the maze with path marked
        """
        # Create a copy of the maze
        visual = [row[:] for row in self.maze]
        
        # Mark the path
        for r, c in path:
            if (r, c) == self.start:
                visual[r][c] = 'S'
            elif (r, c) == self.goal:
                visual[r][c] = 'G'
            else:
                visual[r][c] = '*'
        
        # Convert to string
        return '\n'.join([''.join(row) for row in visual])
    
    def compare_algorithms(self) -> Dict:
        """Compare all pathfinding algorithms on this maze."""
        return {
            'BFS': self.solve_bfs(),
            'DFS': self.solve_dfs(),
            'Dijkstra': self.solve_dijkstra(),
            'A*': self.solve_astar()
        }
    
    @staticmethod
    def create_sample_maze() -> 'MazeProblem':
        """Create a sample maze problem."""
        maze = [
            ['S', '.', '#', '.', '.', '.', '#', '.', '.', '.'],
            ['.', '.', '#', '.', '#', '.', '#', '.', '#', '.'],
            ['.', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
            ['.', '#', '.', '#', '#', '#', '#', '.', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
            ['#', '#', '#', '#', '.', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '#', '#', '#', '#', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'G'],
        ]
        
        start = (0, 0)
        goal = (8, 9)
        
        return MazeProblem(maze, start, goal)
    
    @staticmethod
    def create_complex_maze() -> 'MazeProblem':
        """Create a more complex maze problem."""
        maze = [
            ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
            ['.', '#', '#', '.', '#', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.'],
            ['#', '#', '.', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]
        
        start = (0, 0)
        goal = (8, 14)
        
        return MazeProblem(maze, start, goal)
