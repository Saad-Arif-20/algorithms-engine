# Algorithmic Problem-Solving Engine

A Python application demonstrating discrete structures, algorithm design, and programmatic problem-solving. This project implements multiple pathfinding algorithms, custom data structures, and solves various computational problems.

## Purpose

This project demonstrates proficiency in:
- **Discrete logic and structures** (graphs, trees, queues, stacks)
- **Algorithm selection and complexity analysis**
- **Python as a problem-solving language**
- **Modular software design**

## Core Concepts Demonstrated

### Data Structures (Custom Implementations)
- **Graph**: Directed and undirected graphs with weighted edges
- **Queue**: FIFO data structure using linked list
- **Stack**: LIFO data structure using linked list
- **Priority Queue**: Min-heap implementation for efficient priority operations
- **Binary Tree**: Tree structure with traversal methods

### Algorithms
- **BFS (Breadth-First Search)**: Level-by-level exploration, guarantees shortest path in unweighted graphs
- **DFS (Depth-First Search)**: Deep exploration with backtracking
- **Dijkstra's Algorithm**: Optimal pathfinding in weighted graphs with non-negative edges
- **A* (A-Star)**: Informed search using heuristics for optimal pathfinding

### Problem Types
1. **Pathfinding**: Finding routes in weighted graphs (e.g., city maps)
2. **Maze Solving**: Navigating 2D grid mazes
3. **Scheduling**: Task ordering with dependency management using topological sorting

## Project Structure

```
/algorithms-engine
 ├── algorithms/          # Pathfinding algorithm implementations
 │   ├── __init__.py
 │   ├── bfs.py          # Breadth-First Search
 │   ├── dfs.py          # Depth-First Search
 │   ├── dijkstra.py     # Dijkstra's Algorithm
 │   └── astar.py        # A* Algorithm with heuristics
 │
 ├── data_structures/     # Custom data structure implementations
 │   ├── __init__.py
 │   ├── graph.py        # Graph with nodes and edges
 │   ├── queue.py        # FIFO Queue
 │   ├── stack.py        # LIFO Stack
 │   ├── priority_queue.py  # Min-heap Priority Queue
 │   └── tree.py         # Binary Tree
 │
 ├── problems/           # Problem definitions and solvers
 │   ├── __init__.py
 │   ├── pathfinding.py  # General pathfinding problems
 │   ├── maze.py         # 2D maze navigation
 │   └── scheduling.py   # Task scheduling with dependencies
 │
 ├── tests/              # Comprehensive test suite
 │   ├── test_data_structures.py
 │   ├── test_algorithms.py
 │   └── test_problems.py
 │
 ├── main.py             # Main application demonstrating all features
 └── README.md           # This file
```

## Getting Started

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd algorithms-engine
```

2. Run the main application:
```bash
python main.py
```

3. Run the test suite:
```bash
python -m unittest discover tests
```

## Usage Examples

### Example 1: Pathfinding on City Map

```python
from problems import PathfindingProblem

# Create a city map problem
problem = PathfindingProblem.create_city_map()

# Solve using different algorithms
bfs_result = problem.solve_bfs()
dijkstra_result = problem.solve_dijkstra()
astar_result = problem.solve_astar('euclidean')

# Compare all algorithms
comparison = problem.compare_algorithms()
```

### Example 2: Maze Solving

```python
from problems import MazeProblem

# Create a maze
maze = MazeProblem.create_sample_maze()

# Solve using A*
result = maze.solve_astar()

# Visualize the solution
if result['found']:
    print(maze.visualize_solution(result['path']))
```

### Example 3: Task Scheduling

```python
from problems import SchedulingProblem

# Create a software project
problem = SchedulingProblem.create_software_project()

# Calculate critical path
result = problem.calculate_critical_path()

print(f"Execution order: {result['order']}")
print(f"Total duration: {result['total_duration']} hours")
```

### Example 4: Custom Graph and Algorithm

```python
from data_structures import Graph
from algorithms import dijkstra

# Create a custom graph
graph = Graph(directed=False)
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)

# Find shortest path
result = dijkstra(graph, 'A', 'C')
print(f"Path: {result['path']}")
print(f"Cost: {result['cost']}")
```

## Algorithm Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Use Case |
|-----------|----------------|------------------|----------|
| **BFS** | O(V + E) | O(V) | Unweighted shortest path |
| **DFS** | O(V + E) | O(V) | Path finding, cycle detection |
| **Dijkstra** | O((V + E) log V) | O(V) | Weighted shortest path (non-negative) |
| **A*** | O((V + E) log V)* | O(V) | Optimal with admissible heuristic |

*A* performance depends on heuristic quality. With a good heuristic, it explores fewer nodes than Dijkstra.

Where:
- V = Number of vertices (nodes)
- E = Number of edges

## Testing

The project includes comprehensive unit tests covering:

### Data Structure Tests
- Graph operations (add nodes, edges, neighbors)
- Queue operations (enqueue, dequeue, FIFO property)
- Stack operations (push, pop, LIFO property)
- Priority Queue (heap property, min extraction)
- Binary Tree (insertion, traversals)

### Algorithm Tests
- Path finding correctness
- Shortest path optimality
- Edge cases (no path, single node, etc.)
- Performance comparisons

### Problem Tests
- Pathfinding on various graphs
- Maze solving with different algorithms
- Scheduling with dependency resolution
- Circular dependency detection

Run all tests:
```bash
python -m unittest discover tests -v
```

Run specific test file:
```bash
python -m unittest tests.test_algorithms
```

## Performance Benchmarks

The main application includes performance benchmarking that compares:
- Execution time for each algorithm
- Number of nodes explored
- Path length and optimality

Example output:
```
Algorithm       Time (ms)    Nodes Explored  Path Length
BFS             0.173        45              18
DFS             0.179        38              22
Dijkstra        0.358        42              18
A*              0.440        28              18
```

## 🎓 Learning Context & Academic Alignment

This project demonstrates applied understanding of key computer science concepts:

| Outcome | Implementation Evidence |
| :--- | :--- |
| **Data Structure Design** | Custom implementations of Graph, Queue, Stack, Priority Queue, and Binary Tree from scratch. |
| **Algorithm Analysis** | Complexity analysis and performance benchmarking of BFS, DFS, Dijkstra, and A*. |
| **Problem Decomposition** | Modular architecture separating algorithms, data structures, and problem domains. |
| **Discrete Mathematics** | Application of graph theory, tree traversal, and mathematical optimization. |

**Related Concepts**:
*   Algorithms and data structures
*   Discrete mathematics
*   Programming fundamentals

---


## Key Features

### 1. Custom Data Structures
All data structures are implemented from scratch without using Python's built-in collections (except for basic lists and dictionaries where appropriate):
- No use of `collections.deque`
- No use of `heapq`
- Manual memory management through linked structures

### 2. Modular Design
- Clear separation of concerns
- Reusable components
- Easy to extend with new algorithms or problems

### 3. Algorithm Comparison
- Side-by-side performance metrics
- Visual path comparison
- Complexity analysis

### 4. Real-World Applications
- City route planning
- Maze navigation
- Project scheduling

## Design Decisions

### Why Custom Data Structures?
To demonstrate understanding of fundamental computer science concepts and avoid relying on built-in implementations.

### Why These Algorithms?
- **BFS**: Foundation for graph traversal, guarantees shortest path in unweighted graphs
- **DFS**: Memory-efficient, useful for certain problem types
- **Dijkstra**: Industry standard for weighted shortest path
- **A***: Optimal informed search, widely used in games and robotics

### Graph Representation
Uses adjacency list representation for efficiency:
- Space: O(V + E)
- Neighbor lookup: O(1) average case
- Suitable for sparse graphs

## Limitations and Future Improvements

### Current Limitations
1. **A* Heuristic**: Requires manual position specification for nodes
2. **Negative Weights**: Dijkstra doesn't support negative edge weights
3. **Visualization**: Text-based only, no graphical output

### Potential Improvements
1. **Additional Algorithms**:
   - Bellman-Ford (for negative weights)
   - Floyd-Warshall (all-pairs shortest path)
   - Kruskal's/Prim's (minimum spanning tree)

2. **Enhanced Features**:
   - Graphical visualization using matplotlib
   - Interactive maze generation
   - Real-time algorithm animation
   - Web interface for demonstrations

3. **Performance Optimizations**:
   - Bidirectional search
   - Jump point search for grids
   - Fibonacci heap for Dijkstra

4. **Extended Problem Types**:
   - Network flow problems
   - Traveling salesman problem
   - Graph coloring

## Author

**SAAD ARIF**
**Year**: 2024

Aspiring Computer Science undergraduate (advanced entry)

Background in engineering and software development

## License

This project was created for educational and professional development purposes to consolidate and demonstrate core computer science concepts.

## Acknowledgments

- Classic algorithms from Cormen, Leiserson, Rivest, and Stein (CLRS)
- Graph theory foundations from discrete mathematics
- Computer science education community

---

**Note**: This project demonstrates understanding of algorithms and data structures through practical implementation. All implementations are original and were developed for educational and professional skill consolidation purposes.
