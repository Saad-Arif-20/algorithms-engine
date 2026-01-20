"""
Dijkstra's Algorithm
Finds shortest path in weighted graphs with non-negative edge weights.

Time Complexity: O((V + E) log V) with binary heap
Space Complexity: O(V) for distance map and priority queue
"""

from typing import List, Optional, Dict
from data_structures import Graph, GraphNode, PriorityQueue


def dijkstra(graph: Graph, start_value, goal_value) -> Dict:
    """
    Perform Dijkstra's algorithm to find shortest path from start to goal.
    
    Args:
        graph: The graph to search (must have non-negative weights)
        start_value: Starting node value
        goal_value: Goal node value
    
    Returns:
        Dictionary containing:
        - 'found': Boolean indicating if goal was found
        - 'path': List of node values from start to goal
        - 'cost': Total cost of the path
        - 'visited': List of all visited nodes in order
        - 'nodes_explored': Number of nodes explored
    """
    start_node = graph.get_node(start_value)
    goal_node = graph.get_node(goal_value)
    
    if not start_node or not goal_node:
        return {
            'found': False,
            'path': [],
            'cost': float('inf'),
            'visited': [],
            'nodes_explored': 0
        }
    
    # Initialize distances and parent tracking
    distance: Dict[GraphNode, float] = {node: float('inf') for node in graph.get_all_nodes()}
    distance[start_node] = 0
    
    parent: Dict[GraphNode, Optional[GraphNode]] = {start_node: None}
    visited = set()
    visited_order = []
    
    # Priority queue: (distance, node)
    pq = PriorityQueue()
    pq.insert(start_node, 0)
    
    while not pq.is_empty():
        current_dist, current = pq.extract_min()
        
        if current in visited:
            continue
        
        visited.add(current)
        visited_order.append(current.value)
        
        # Early exit if we reached the goal
        if current == goal_node:
            # Reconstruct path
            path = []
            node = goal_node
            while node is not None:
                path.append(node.value)
                node = parent.get(node)
            path.reverse()
            
            return {
                'found': True,
                'path': path,
                'cost': distance[goal_node],
                'visited': visited_order,
                'nodes_explored': len(visited)
            }
        
        # Explore neighbors
        for neighbor in current.get_neighbors():
            if neighbor in visited:
                continue
            
            edge_weight = current.get_weight(neighbor)
            new_distance = distance[current] + edge_weight
            
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                parent[neighbor] = current
                pq.insert(neighbor, new_distance)
    
    return {
        'found': False,
        'path': [],
        'cost': float('inf'),
        'visited': visited_order,
        'nodes_explored': len(visited)
    }


def dijkstra_path(graph: Graph, start_value, goal_value) -> Optional[List]:
    """
    Simplified Dijkstra that returns just the path.
    
    Returns:
        List of node values representing the shortest path, or None if no path exists
    """
    result = dijkstra(graph, start_value, goal_value)
    return result['path'] if result['found'] else None
