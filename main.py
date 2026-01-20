"""
Algorithmic Problem-Solving Engine
Main application demonstrating various algorithms and data structures.

Author: SAAD ARIF
Purpose: Demonstrate discrete structures, algorithm design, and programmatic thinking
"""

import time
from problems import PathfindingProblem, MazeProblem, SchedulingProblem


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_section(title):
    """Print a section divider."""
    print(f"\n--- {title} ---")


def demonstrate_pathfinding():
    """Demonstrate pathfinding algorithms on a city map."""
    print_header("PATHFINDING: European Cities")
    
    problem = PathfindingProblem.create_city_map()
    print(f"\nFinding path from {problem.start} to {problem.goal}")
    print(f"Graph has {len(problem.graph)} cities")
    
    # Compare all algorithms
    results = problem.compare_algorithms()
    
    print_section("Algorithm Comparison")
    print(f"{'Algorithm':<20} {'Found':<8} {'Cost':<10} {'Nodes Explored':<15} {'Path Length':<12}")
    print("-" * 80)
    
    for algo_name, result in results.items():
        found = "Yes" if result['found'] else "No"
        cost_value = result.get('cost')
        if cost_value is not None and cost_value != float('inf'):
            cost = f"{cost_value:.1f}"
        else:
            cost = "N/A"
        nodes = result['nodes_explored']
        path_len = len(result['path'])
        
        print(f"{algo_name:<20} {found:<8} {cost:<10} {nodes:<15} {path_len:<12}")
    
    # Show the optimal path
    dijkstra_result = results['Dijkstra']
    if dijkstra_result['found']:
        print_section("Optimal Path (Dijkstra)")
        print(" -> ".join(dijkstra_result['path']))
        print(f"Total Distance: {dijkstra_result['cost']:.1f} km")


def demonstrate_maze_solving():
    """Demonstrate maze solving with different algorithms."""
    print_header("MAZE SOLVING")
    
    maze = MazeProblem.create_sample_maze()
    print(f"\nMaze size: {maze.rows}x{maze.cols}")
    print(f"Start: {maze.start}, Goal: {maze.goal}")
    
    # Show original maze
    print_section("Original Maze")
    for row in maze.maze:
        print(''.join(row))
    
    # Compare algorithms
    results = maze.compare_algorithms()
    
    print_section("Algorithm Performance")
    print(f"{'Algorithm':<15} {'Found':<8} {'Path Length':<12} {'Nodes Explored':<15}")
    print("-" * 60)
    
    for algo_name, result in results.items():
        found = "Yes" if result['found'] else "No"
        path_len = len(result['path'])
        nodes = result['nodes_explored']
        
        print(f"{algo_name:<15} {found:<8} {path_len:<12} {nodes:<15}")
    
    # Visualize BFS solution
    bfs_result = results['BFS']
    if bfs_result['found']:
        print_section("Solution Path (BFS)")
        visual = maze.visualize_solution(bfs_result['path'])
        print(visual)
        print("\nLegend: S=Start, G=Goal, *=Path, #=Wall, .=Open")


def demonstrate_scheduling():
    """Demonstrate task scheduling with dependencies."""
    print_header("TASK SCHEDULING: Software Project")
    
    problem = SchedulingProblem.create_software_project()
    print(f"\nTotal tasks: {len(problem.tasks)}")
    
    # Show all tasks
    print_section("Project Tasks")
    print(f"{'Task':<20} {'Duration (hours)':<15}")
    print("-" * 40)
    for task_name, task in problem.tasks.items():
        print(f"{task_name:<20} {task.duration:<15}")
    
    # Calculate critical path
    result = problem.calculate_critical_path()
    
    if result['error']:
        print(f"\nError: {result['error']}")
        return
    
    print_section("Execution Order (Topological Sort)")
    for i, task_name in enumerate(result['order'], 1):
        print(f"{i}. {task_name}")
    
    print_section("Task Schedule")
    print(f"{'Task':<20} {'Start Time':<15} {'Duration':<10} {'End Time':<10}")
    print("-" * 60)
    
    for task_name in result['order']:
        task = problem.tasks[task_name]
        start = result['earliest_start'][task_name]
        end = start + task.duration
        print(f"{task_name:<20} {start:<15} {task.duration:<10} {end:<10}")
    
    print(f"\nTotal Project Duration: {result['total_duration']} hours")
    print(f"Estimated Days (8h/day): {result['total_duration'] / 8:.1f} days")


def run_performance_benchmark():
    """Benchmark algorithm performance."""
    print_header("PERFORMANCE BENCHMARK")
    
    # Create a larger maze for benchmarking
    print("\nCreating complex maze for performance testing...")
    maze = MazeProblem.create_complex_maze()
    
    algorithms = {
        'BFS': maze.solve_bfs,
        'DFS': maze.solve_dfs,
        'Dijkstra': maze.solve_dijkstra,
        'A*': maze.solve_astar
    }
    
    print_section("Execution Time Comparison")
    print(f"{'Algorithm':<15} {'Time (ms)':<12} {'Nodes Explored':<15} {'Path Length':<12}")
    print("-" * 60)
    
    for algo_name, solve_func in algorithms.items():
        start_time = time.time()
        result = solve_func()
        end_time = time.time()
        
        elapsed_ms = (end_time - start_time) * 1000
        nodes = result['nodes_explored']
        path_len = len(result['path']) if result['found'] else 0
        
        print(f"{algo_name:<15} {elapsed_ms:<12.3f} {nodes:<15} {path_len:<12}")


def show_complexity_analysis():
    """Display complexity analysis of algorithms."""
    print_header("ALGORITHM COMPLEXITY ANALYSIS")
    
    complexities = [
        ("BFS", "O(V + E)", "O(V)", "Unweighted shortest path"),
        ("DFS", "O(V + E)", "O(V)", "Path finding, cycle detection"),
        ("Dijkstra", "O((V + E) log V)", "O(V)", "Weighted shortest path (non-negative)"),
        ("A*", "O((V + E) log V)", "O(V)", "Optimal with admissible heuristic"),
    ]
    
    print(f"\n{'Algorithm':<12} {'Time':<20} {'Space':<10} {'Use Case':<40}")
    print("-" * 85)
    
    for algo, time_comp, space_comp, use_case in complexities:
        print(f"{algo:<12} {time_comp:<20} {space_comp:<10} {use_case:<40}")
    
    print("\nWhere:")
    print("  V = Number of vertices (nodes)")
    print("  E = Number of edges")


def main():
    """Main application entry point."""
    print("\n" + "=" * 80)
    print("  ALGORITHMIC PROBLEM-SOLVING ENGINE")
    print("  Demonstrating Discrete Structures & Algorithm Design")
    print("=" * 80)
    
    try:
        # Run all demonstrations
        demonstrate_pathfinding()
        demonstrate_maze_solving()
        demonstrate_scheduling()
        run_performance_benchmark()
        show_complexity_analysis()
        
        print_header("DEMONSTRATION COMPLETE")
        print("\nAll algorithms executed successfully!")
        print("\nKey Achievements:")
        print("  [+] Custom data structures (Graph, Queue, Stack, Priority Queue, Tree)")
        print("  [+] Pathfinding algorithms (BFS, DFS, Dijkstra, A*)")
        print("  [+] Problem-solving applications (Pathfinding, Maze, Scheduling)")
        print("  [+] Algorithm comparison and complexity analysis")
        print("  [+] Modular, maintainable code architecture")
        
        print("\nTo run tests:")
        print("  python -m unittest discover tests")
        
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
