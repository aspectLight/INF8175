# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Direction]:
    stack = util.Stack()
    start = problem.getStartState()
    stack.push((start, []))
    visited = set()

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state in visited:
            continue
        visited.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))

    return []


def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    stack = util.Queue()
    start = problem.getStartState()
    stack.push((start, []))
    visited = set()

    while not stack.isEmpty():
        state, actions = stack.pop()

        if problem.isGoalState(state):
            return actions

        if state in visited:
            continue
        visited.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in visited:
                stack.push((successor, actions + [action]))

    return []

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    pq = util.PriorityQueue()
    start = problem.getStartState()
    pq.push((start, [], 0), 0) 
    visited = set()

    while not pq.isEmpty():
        state, actions, cost = pq.pop()  

        if problem.isGoalState(state):
            return actions

        if state in visited:
            continue
        visited.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in visited:
                new_cost = cost + step_cost
                pq.push((successor, actions + [action], new_cost), new_cost)

    return []

def nullHeuristic(state:GameState, problem:SearchProblem=None)->int:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    pq = util.PriorityQueue()
    start = problem.getStartState()
    pq.push((start, [], 0 ), heuristic(start, problem))  
    visited = set()

    while not pq.isEmpty():
        state, actions, g_cost = pq.pop()  

        if problem.isGoalState(state):
            return actions

        if state in visited:
            continue
        visited.add(state)

        for successor, action, step_cost in problem.getSuccessors(state):
            if successor not in visited:
                new_g_cost = g_cost + step_cost
                f_cost = new_g_cost + heuristic(successor, problem) 
                pq.push((successor, actions + [action], new_g_cost), f_cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
