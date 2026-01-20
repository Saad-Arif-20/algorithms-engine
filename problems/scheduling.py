"""
Scheduling Problem
Task scheduling with dependencies using topological sorting.
"""

from typing import List, Dict, Set, Optional
from data_structures import Graph, Queue


class Task:
    """Represents a task with duration and dependencies."""
    
    def __init__(self, name: str, duration: int):
        self.name = name
        self.duration = duration
        self.dependencies: List['Task'] = []
    
    def add_dependency(self, task: 'Task'):
        """Add a task that must be completed before this one."""
        self.dependencies.append(task)
    
    def __repr__(self):
        return f"Task({self.name}, {self.duration}h)"


class SchedulingProblem:
    """
    Represents a task scheduling problem with dependencies.
    Uses topological sorting to find valid execution order.
    """
    
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.graph = Graph(directed=True)
    
    def add_task(self, name: str, duration: int) -> Task:
        """Add a task to the scheduling problem."""
        if name not in self.tasks:
            task = Task(name, duration)
            self.tasks[name] = task
            self.graph.add_node(name)
        return self.tasks[name]
    
    def add_dependency(self, task_name: str, depends_on: str):
        """
        Add a dependency: task_name depends on depends_on.
        depends_on must be completed before task_name can start.
        """
        if task_name not in self.tasks or depends_on not in self.tasks:
            raise ValueError("Both tasks must exist")
        
        self.tasks[task_name].add_dependency(self.tasks[depends_on])
        # Edge from dependency to dependent (depends_on -> task_name)
        self.graph.add_edge(depends_on, task_name)
    
    def topological_sort(self) -> Optional[List[str]]:
        """
        Perform topological sort using Kahn's algorithm.
        
        Returns:
            List of task names in valid execution order, or None if cycle detected
        """
        # Calculate in-degree for each node
        in_degree: Dict[str, int] = {name: 0 for name in self.tasks}
        
        for task_name in self.tasks:
            neighbors = self.graph.get_neighbors(task_name)
            for neighbor in neighbors:
                in_degree[neighbor.value] += 1
        
        # Queue of tasks with no dependencies
        queue = Queue()
        for task_name, degree in in_degree.items():
            if degree == 0:
                queue.enqueue(task_name)
        
        result = []
        
        while not queue.is_empty():
            current = queue.dequeue()
            result.append(current)
            
            # Reduce in-degree of neighbors
            neighbors = self.graph.get_neighbors(current)
            for neighbor in neighbors:
                in_degree[neighbor.value] -= 1
                if in_degree[neighbor.value] == 0:
                    queue.enqueue(neighbor.value)
        
        # Check if all tasks were processed (no cycle)
        if len(result) != len(self.tasks):
            return None  # Cycle detected
        
        return result
    
    def calculate_critical_path(self) -> Dict:
        """
        Calculate the critical path (longest path) through the task graph.
        
        Returns:
            Dictionary with:
            - 'order': Topological order of tasks
            - 'earliest_start': Earliest start time for each task
            - 'total_duration': Minimum project completion time
            - 'critical_path': Tasks on the critical path
        """
        order = self.topological_sort()
        
        if order is None:
            return {
                'error': 'Circular dependency detected',
                'order': None,
                'earliest_start': None,
                'total_duration': None,
                'critical_path': None
            }
        
        # Calculate earliest start times
        earliest_start: Dict[str, int] = {name: 0 for name in self.tasks}
        
        for task_name in order:
            task = self.tasks[task_name]
            
            # Earliest start is max(end time of all dependencies)
            for dep in task.dependencies:
                dep_end = earliest_start[dep.name] + dep.duration
                earliest_start[task_name] = max(earliest_start[task_name], dep_end)
        
        # Calculate total project duration
        total_duration = 0
        for task_name in self.tasks:
            task = self.tasks[task_name]
            end_time = earliest_start[task_name] + task.duration
            total_duration = max(total_duration, end_time)
        
        return {
            'order': order,
            'earliest_start': earliest_start,
            'total_duration': total_duration,
            'error': None
        }
    
    @staticmethod
    def create_software_project() -> 'SchedulingProblem':
        """Create a sample software development project scheduling problem."""
        problem = SchedulingProblem()
        
        # Add tasks (name, duration in hours)
        problem.add_task('Requirements', 8)
        problem.add_task('Design', 16)
        problem.add_task('Database', 12)
        problem.add_task('Backend', 24)
        problem.add_task('Frontend', 20)
        problem.add_task('Testing', 16)
        problem.add_task('Deployment', 4)
        problem.add_task('Documentation', 8)
        
        # Add dependencies
        problem.add_dependency('Design', 'Requirements')
        problem.add_dependency('Database', 'Design')
        problem.add_dependency('Backend', 'Database')
        problem.add_dependency('Frontend', 'Design')
        problem.add_dependency('Testing', 'Backend')
        problem.add_dependency('Testing', 'Frontend')
        problem.add_dependency('Deployment', 'Testing')
        problem.add_dependency('Documentation', 'Testing')
        
        return problem
