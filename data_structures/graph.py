"""
Custom Graph Implementation
Supports both directed and undirected graphs with weighted edges.
"""

from typing import Dict, List, Set, Optional, Tuple


class GraphNode:
    """Represents a node in the graph."""
    
    def __init__(self, value):
        self.value = value
        self.neighbors: Dict['GraphNode', float] = {}  # neighbor -> weight
    
    def add_neighbor(self, neighbor: 'GraphNode', weight: float = 1.0):
        """Add a neighbor with an optional weight."""
        self.neighbors[neighbor] = weight
    
    def get_neighbors(self) -> List['GraphNode']:
        """Return list of neighboring nodes."""
        return list(self.neighbors.keys())
    
    def get_weight(self, neighbor: 'GraphNode') -> float:
        """Get the weight of edge to a neighbor."""
        return self.neighbors.get(neighbor, float('inf'))
    
    def __repr__(self):
        return f"GraphNode({self.value})"
    
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        if not isinstance(other, GraphNode):
            return False
        return self.value == other.value


class Graph:
    """
    Custom Graph implementation supporting:
    - Directed and undirected graphs
    - Weighted edges
    - Node and edge operations
    """
    
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: Dict[any, GraphNode] = {}
    
    def add_node(self, value) -> GraphNode:
        """Add a node to the graph."""
        if value not in self.nodes:
            self.nodes[value] = GraphNode(value)
        return self.nodes[value]
    
    def add_edge(self, from_value, to_value, weight: float = 1.0):
        """Add an edge between two nodes."""
        from_node = self.add_node(from_value)
        to_node = self.add_node(to_value)
        
        from_node.add_neighbor(to_node, weight)
        if not self.directed:
            to_node.add_neighbor(from_node, weight)
    
    def get_node(self, value) -> Optional[GraphNode]:
        """Get a node by its value."""
        return self.nodes.get(value)
    
    def get_all_nodes(self) -> List[GraphNode]:
        """Return all nodes in the graph."""
        return list(self.nodes.values())
    
    def get_neighbors(self, value) -> List[GraphNode]:
        """Get neighbors of a node."""
        node = self.get_node(value)
        return node.get_neighbors() if node else []
    
    def get_edge_weight(self, from_value, to_value) -> float:
        """Get the weight of an edge."""
        from_node = self.get_node(from_value)
        to_node = self.get_node(to_value)
        
        if from_node and to_node:
            return from_node.get_weight(to_node)
        return float('inf')
    
    def __len__(self):
        return len(self.nodes)
    
    def __repr__(self):
        return f"Graph(nodes={len(self.nodes)}, directed={self.directed})"
