"""
Breadth-First Search (BFS) Algorithm
Explores nodes level by level, guarantees shortest path in unweighted graphs.

Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V) for the queue and visited set
"""

from typing import List, Optional, Set, Dict
from data_structures import Graph, GraphNode, Queue


def breadth_first_search(graph: Graph, start_value, goal_value) -> Dict:
    """
    Perform BFS to find a path from start to goal.
    
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
    
    queue = Queue()
    queue.enqueue(start_node)
    
    visited: Set[GraphNode] = set()
    visited.add(start_node)
    
    parent: Dict[GraphNode, Optional[GraphNode]] = {start_node: None}
    visited_order: List = [start_value]
    
    while not queue.is_empty():
        current = queue.dequeue()
        
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
        
        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.enqueue(neighbor)
                visited_order.append(neighbor.value)
    
    return {
        'found': False,
        'path': [],
        'visited': visited_order,
        'nodes_explored': len(visited)
    }


def bfs_path(graph: Graph, start_value, goal_value) -> Optional[List]:
    """
    Simplified BFS that returns just the path.
    
    Returns:
        List of node values representing the path, or None if no path exists
    """
    result = breadth_first_search(graph, start_value, goal_value)
    return result['path'] if result['found'] else None
