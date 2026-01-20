"""
A* (A-Star) Algorithm
Informed search algorithm using heuristics for optimal pathfinding.

Time Complexity: O((V + E) log V) with binary heap (depends on heuristic quality)
Space Complexity: O(V) for distance maps and priority queue
"""

from typing import List, Optional, Dict, Callable
from data_structures import Graph, GraphNode, PriorityQueue


def astar(graph: Graph, start_value, goal_value, heuristic: Callable[[any, any], float]) -> Dict:
    """
    Perform A* algorithm to find optimal path from start to goal using a heuristic.
    
    Args:
        graph: The graph to search
        start_value: Starting node value
        goal_value: Goal node value
        heuristic: Function that estimates cost from a node to goal
                   Should take (node_value, goal_value) and return float
    
    Returns:
        Dictionary containing:
        - 'found': Boolean indicating if goal was found
        - 'path': List of node values from start to goal
        - 'cost': Total actual cost of the path
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
    
    # g_score: actual cost from start to node
    g_score: Dict[GraphNode, float] = {node: float('inf') for node in graph.get_all_nodes()}
    g_score[start_node] = 0
    
    # f_score: g_score + heuristic (estimated total cost)
    f_score: Dict[GraphNode, float] = {node: float('inf') for node in graph.get_all_nodes()}
    f_score[start_node] = heuristic(start_value, goal_value)
    
    parent: Dict[GraphNode, Optional[GraphNode]] = {start_node: None}
    visited = set()
    visited_order = []
    
    # Priority queue: (f_score, node)
    pq = PriorityQueue()
    pq.insert(start_node, f_score[start_node])
    
    while not pq.is_empty():
        current_f, current = pq.extract_min()
        
        if current in visited:
            continue
        
        visited.add(current)
        visited_order.append(current.value)
        
        # Goal reached
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
                'cost': g_score[goal_node],
                'visited': visited_order,
                'nodes_explored': len(visited)
            }
        
        # Explore neighbors
        for neighbor in current.get_neighbors():
            if neighbor in visited:
                continue
            
            tentative_g_score = g_score[current] + current.get_weight(neighbor)
            
            if tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better
                parent[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor.value, goal_value)
                pq.insert(neighbor, f_score[neighbor])
    
    return {
        'found': False,
        'path': [],
        'cost': float('inf'),
        'visited': visited_order,
        'nodes_explored': len(visited)
    }


def astar_path(graph: Graph, start_value, goal_value, heuristic: Callable[[any, any], float]) -> Optional[List]:
    """
    Simplified A* that returns just the path.
    
    Returns:
        List of node values representing the optimal path, or None if no path exists
    """
    result = astar(graph, start_value, goal_value, heuristic)
    return result['path'] if result['found'] else None


# Common heuristic functions
def manhattan_distance(pos1: tuple, pos2: tuple) -> float:
    """
    Manhattan distance heuristic for grid-based problems.
    Assumes positions are (x, y) tuples.
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def euclidean_distance(pos1: tuple, pos2: tuple) -> float:
    """
    Euclidean distance heuristic.
    Assumes positions are (x, y) tuples.
    """
    return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5


def zero_heuristic(node1: any, node2: any) -> float:
    """
    Zero heuristic (makes A* behave like Dijkstra).
    """
    return 0.0
