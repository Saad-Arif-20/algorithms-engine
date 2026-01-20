"""
Depth-First Search (DFS) Algorithm
Explores as far as possible along each branch before backtracking.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) for the stack and visited set
"""

from typing import List, Optional, Set, Dict
from data_structures import Graph, GraphNode, Stack


def depth_first_search(graph: Graph, start_value, goal_value) -> Dict:
    """
    Perform DFS to find a path from start to goal.
    
    Args:
        graph: The graph to search
        start_value: Starting node value
        goal_value: Goal node value
    
    Returns:
        Dictionary containing:
        - 'found': Boolean indicating if goal was found
        - 'path': List of node values from start to goal
        - 'visited': List of all visited nodes in order
        - 'nodes_explored': Number of nodes explored
    """
    start_node = graph.get_node(start_value)
    goal_node = graph.get_node(goal_value)
    
    if not start_node or not goal_node:
        return {
            'found': False,
            'path': [],
            'visited': [],
            'nodes_explored': 0
        }
    
    stack = Stack()
    stack.push(start_node)
    
    visited: Set[GraphNode] = set()
    parent: Dict[GraphNode, Optional[GraphNode]] = {start_node: None}
    visited_order: List = []
    
    while not stack.is_empty():
        current = stack.pop()
        
        if current in visited:
            continue
        
        visited.add(current)
        visited_order.append(current.value)
        
        if current == goal_node:
            # Reconstruct path
            path = []
            node = goal_node
            while node is not None:
                path.append(node.value)
                node = parent[node]
            path.reverse()
            
            return {
                'found': True,
                'path': path,
                'visited': visited_order,
                'nodes_explored': len(visited)
            }
        
        # Push neighbors onto stack (reverse order for consistent exploration)
        neighbors = current.get_neighbors()
        for neighbor in reversed(neighbors):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current
                stack.push(neighbor)
    
    return {
        'found': False,
        'path': [],
        'visited': visited_order,
        'nodes_explored': len(visited)
    }


def dfs_path(graph: Graph, start_value, goal_value) -> Optional[List]:
    """
    Simplified DFS that returns just the path.
    
    Returns:
        List of node values representing the path, or None if no path exists
    """
    result = depth_first_search(graph, start_value, goal_value)
    return result['path'] if result['found'] else None
