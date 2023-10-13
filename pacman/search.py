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

import util
# import searchAgents  # Importing the Manhattan heuristic

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = util.Stack()  # stack 
    stack.push((problem.getStartState(), []))
    # initialize explored 
    explored = set()
    while not stack.isEmpty():
        node, actions = stack.pop()
        if problem.isGoalState(node):
            return actions
        if node not in explored:
            explored.add(node)
            for successor, action, stepCost in problem.getSuccessors(node):
                if successor not in explored and successor not in (item[0] for item in stack.list):
                    stack.push((successor, actions + [action]))
    return []
    util.raiseNotDefined()
    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()  # queue 
    queue.push((problem.getStartState(), []))  
    explored = set()
    
    # while the frontier is not empty:
    while not queue.isEmpty():
        node, actions = queue.pop()
        # if the node contains a goal state:
        if problem.isGoalState(node):
            return actions
        # add state key 
        explored.add(node)
        for successor, action, stepCost in problem.getSuccessors(node):
            if successor not in explored and successor not in (item[0] for item in queue.list):
                queue.push((successor, actions + [action]))
    
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    queue = util.PriorityQueue()  #  priority queue
    queue.push((problem.getStartState(), [], 0), 0)  #  tuple of (state, actions, cost)
    # initialize explored 
    explored = set()
    while not queue.isEmpty():
        node, actions, cost = queue.pop()
        if problem.isGoalState(node):
            return actions
        if node not in explored:
            explored.add(node)
            for successor, action, stepCost in problem.getSuccessors(node):
                if successor not in explored:
                    newCost = cost + stepCost
                    #  new cost as the priority
                    queue.push((successor, actions + [action], newCost), newCost)
    
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def manhattanHeuristic(position, problem, info={}):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def aStarSearch(problem, heuristic=manhattanHeuristic): 
    """Search the node that has the lowest combined cost and heuristic first."""
    #manhattanHeuristic, calculating distance betwween pacman position and the problem goal aka dot
    queue = util.PriorityQueue()  # priority queue
    queue.push((problem.getStartState(), [], 0), 0) 
    explored = set()
    while not queue.isEmpty():
        node, actions, cost = queue.pop()
        if problem.isGoalState(node):
            return actions
        if node not in explored:
            explored.add(node)
            for successor, action, stepCost in problem.getSuccessors(node):
                if successor not in explored:
                    newCost = cost + stepCost
                    priority = newCost + heuristic(successor, problem)
                    queue.push((successor, actions + [action], newCost), priority)
    
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
