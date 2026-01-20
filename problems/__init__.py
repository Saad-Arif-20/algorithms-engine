"""
Problems Module
Defines various problem types that can be solved using the algorithms.
"""

from .pathfinding import PathfindingProblem
from .maze import MazeProblem
from .scheduling import SchedulingProblem

__all__ = [
    'PathfindingProblem',
    'MazeProblem',
    'SchedulingProblem'
]
