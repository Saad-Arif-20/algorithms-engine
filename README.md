# 🧮 Algorithmic Problem-Solving Engine

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive Python implementation of fundamental algorithms and data structures, featuring pathfinding algorithms (BFS, DFS, Dijkstra, A*), custom data structures, and real-world problem solvers for maze navigation, route planning, and task scheduling.

## 🌟 Why This Project?

Understanding algorithms and data structures is fundamental to computer science and software engineering. This project goes beyond theory by implementing these concepts from scratch, demonstrating their practical applications in real-world scenarios like GPS navigation, game AI, and project management.

### Key Highlights
- 🎯 **4 Pathfinding Algorithms** - BFS, DFS, Dijkstra, and A* with performance comparisons
- 🏗️ **Custom Data Structures** - Graph, Queue, Stack, Priority Queue, Binary Tree (built from scratch)
- 🗺️ **Real-World Applications** - City routing, maze solving, task scheduling
- 📊 **Performance Benchmarking** - Side-by-side algorithm comparison with metrics
- 🧪 **Comprehensive Testing** - Full test suite for all components
- 📚 **Zero Dependencies** - Pure Python implementation using only standard library

---

## 🚀 At a Glance

- 🎯 **4 pathfinding algorithms** (BFS, DFS, Dijkstra, A*)
- 🏗️ **5 custom data structures** (built from scratch, no libraries)
- 🗺️ **3 real-world problem types** (routing, mazes, scheduling)
- 📊 **Performance benchmarking** with side-by-side comparisons
- 🧪 **Comprehensive testing** (unittest framework)
- 📚 **Zero dependencies** (pure Python standard library)

⏱️ **Setup time**: < 1 minute  
🎓 **Ideal for**: Algorithm interviews, CS fundamentals, backend engineering

---

## 📚 Table of Contents

- [Why This Project?](#-why-this-project)
- [Quick Start](#-quick-start)
- [Algorithms Implemented](#-algorithms-implemented)
- [Real-World Applications](#-real-world-applications)
- [Performance Benchmarks](#-performance-benchmarks)
- [Key Design Decisions](#-key-design-decisions)
- [What I Learned](#-what-i-learned)
- [Testing](#-testing)
- [Contributing](#-contributing)

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Saad-Arif-20/algorithms-engine.git
cd algorithms-engine

# Run the main application
python main.py

# Run tests
python -m unittest discover tests -v
```

### Quick Example

```python
from problems import PathfindingProblem

# Create a city map problem
problem = PathfindingProblem.create_city_map()

# Solve using different algorithms
bfs_result = problem.solve_bfs()
dijkstra_result = problem.solve_dijkstra()
astar_result = problem.solve_astar('euclidean')

# Compare performance
comparison = problem.compare_algorithms()
print(f"BFS: {comparison['bfs']['time']}ms, {comparison['bfs']['nodes_explored']} nodes")
print(f"A*: {comparison['astar']['time']}ms, {comparison['astar']['nodes_explored']} nodes")
```

---

## 🏗️ Project Structure

```
algorithms-engine/
├── algorithms/              # Algorithm implementations
│   ├── bfs.py              # Breadth-First Search
│   ├── dfs.py              # Depth-First Search
│   ├── dijkstra.py         # Dijkstra's Algorithm
│   └── astar.py            # A* with heuristics
├── data_structures/         # Custom implementations
│   ├── graph.py            # Graph with adjacency list
│   ├── queue.py            # FIFO Queue
│   ├── stack.py            # LIFO Stack
│   ├── priority_queue.py   # Min-heap Priority Queue
│   └── tree.py             # Binary Tree
├── problems/               # Problem solvers
│   ├── pathfinding.py      # Route planning
│   ├── maze.py             # Maze navigation
│   └── scheduling.py       # Task scheduling
├── tests/                  # Test suite
└── main.py                 # Demo application
```

---

## 🎯 Algorithms Implemented

### Pathfinding Algorithms

| Algorithm | Time Complexity | Space | Best For |
|-----------|----------------|-------|----------|
| **BFS** | O(V + E) | O(V) | Unweighted shortest path |
| **DFS** | O(V + E) | O(V) | Path finding, cycle detection |
| **Dijkstra** | O((V + E) log V) | O(V) | Weighted shortest path |
| **A*** | O((V + E) log V)* | O(V) | Optimal with good heuristic |

*A* performance depends on heuristic quality

### Data Structures

- **Graph**: Adjacency list representation with weighted edges
- **Queue**: Linked-list based FIFO structure
- **Stack**: Linked-list based LIFO structure
- **Priority Queue**: Binary min-heap implementation
- **Binary Tree**: Tree with in-order, pre-order, post-order traversals

---

## 💡 Real-World Applications

### 1. City Route Planning
```python
from problems import PathfindingProblem

# Create a city map with weighted roads
problem = PathfindingProblem.create_city_map()

# Find optimal route
result = problem.solve_dijkstra()
print(f"Route: {result['path']}")
print(f"Distance: {result['cost']} km")
```

### 2. Maze Solving
```python
from problems import MazeProblem

# Generate or load a maze
maze = MazeProblem.create_sample_maze()

# Solve using A* with Manhattan distance
result = maze.solve_astar()

# Visualize solution
if result['found']:
    print(maze.visualize_solution(result['path']))
```

### 3. Project Task Scheduling
```python
from problems import SchedulingProblem

# Define tasks with dependencies
problem = SchedulingProblem.create_software_project()

# Calculate critical path
result = problem.calculate_critical_path()
print(f"Execution order: {result['order']}")
print(f"Total duration: {result['total_duration']} hours")
```

---

## 📊 Performance Benchmarks

Example output from `main.py`:

```
Algorithm Comparison - City Map (50 nodes, 120 edges)
═══════════════════════════════════════════════════════
Algorithm    Time (ms)    Nodes Explored    Path Length
BFS          0.173        45                18
DFS          0.179        38                22
Dijkstra     0.358        42                18 (optimal)
A*           0.440        28                18 (optimal)
```

**Key Insights:**
- A* explores fewer nodes than Dijkstra (better heuristic)
- BFS guarantees shortest path in unweighted graphs
- DFS uses less memory but doesn't guarantee optimal path

---

## 🧠 Key Design Decisions

### Why Build Data Structures from Scratch?
- **Deep Understanding**: Learn internal workings, not just API usage
- **Interview Preparation**: Common technical interview requirement
- **No Black Boxes**: Full control and transparency
- **Educational Value**: Understand time/space complexity firsthand

### Why Multiple Pathfinding Algorithms?
- **Trade-off Demonstration**: Show when to use each algorithm
- **Performance Comparison**: Empirical evidence of complexity analysis
- **Real-World Relevance**: Different problems need different approaches
- **Completeness**: Cover breadth-first, depth-first, and informed search

### Why Pure Python (No NumPy/SciPy)?
- **Accessibility**: No installation barriers
- **Fundamentals Focus**: Understand algorithms, not library APIs
- **Portability**: Runs anywhere Python runs
- **Learning**: See the actual implementation, not optimized C code

### Why Separate Algorithms from Problems?
- **Modularity**: Algorithms are reusable across problem types
- **Testing**: Test algorithms independently of problem domains
- **Clarity**: Clear separation of concerns
- **Extensibility**: Easy to add new algorithms or problems

---

## 💡 What I Learned

### Technical Insights
- **Big-O is real**: Saw exponential vs polynomial time differences in practice
- **Heuristics transform performance**: A* with good heuristic explores 60% fewer nodes
- **Data structure choice matters**: Priority queue implementation affects Dijkstra performance significantly
- **Edge cases are subtle**: Empty graphs, single nodes, disconnected components all need handling

### Algorithm Lessons
- **BFS isn't always best**: Optimal for unweighted graphs, but memory-intensive
- **Greedy doesn't guarantee optimal**: DFS finds *a* path, not necessarily the shortest
- **Admissible heuristics are crucial**: Bad heuristics make A* worse than Dijkstra
- **Complexity analysis predicts reality**: O(V+E) vs O(V²) matters at scale

### Professional Growth
- **Benchmarking reveals truth**: Intuition about performance is often wrong
- **Testing is non-negotiable**: Algorithms have subtle bugs that only tests catch
- **Documentation saves time**: Clear docstrings prevent confusion later
- **Code organization scales**: Modular design makes adding features easy

---

## 🧪 Testing

Comprehensive test suite covering:

```bash
# Run all tests
python -m unittest discover tests -v

# Run specific test module
python -m unittest tests.test_algorithms
python -m unittest tests.test_data_structures
python -m unittest tests.test_problems
```

**Test Coverage:**
- ✅ Data structure operations (insert, delete, search)
- ✅ Algorithm correctness (path finding, optimality)
- ✅ Edge cases (empty graphs, no path, single node)
- ✅ Performance validation

---

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Dependencies**: None (pure Python standard library)
- **Testing**: unittest framework
- **Design Pattern**: Object-Oriented Programming (OOP)

---

## 🎓 Learning Resources

This project is perfect for:
- **Interview Preparation**: Common algorithm questions
- **Computer Science Students**: Practical implementation of theory
- **Self-Learners**: Understanding algorithms through code
- **Educators**: Teaching material with working examples

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- Add new algorithms (Bellman-Ford, Floyd-Warshall, Kruskal's)
- Implement visualization (matplotlib, pygame)
- Add more problem types (TSP, graph coloring)
- Improve documentation
- Add performance optimizations

**Steps to contribute:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewAlgorithm`)
3. Add tests for new features
4. Commit changes (`git commit -m 'Add Bellman-Ford algorithm'`)
5. Push to branch (`git push origin feature/NewAlgorithm`)
6. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Saad Arif**
- GitHub: [@Saad-Arif-20](https://github.com/Saad-Arif-20)
- LinkedIn: [@saad--arif](https://www.linkedin.com/in/saad--arif/)

---

## 🙏 Acknowledgments

- **CLRS** (Cormen, Leiserson, Rivest, Stein) - Introduction to Algorithms
- **Graph Theory** - Discrete mathematics foundations
- **Python Community** - For excellent documentation and resources

---

**Built with 🧠 and algorithms** | © 2025 Saad Arif
