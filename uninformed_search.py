# Author: Minh Nguyen, Date: 10/02/2025

from collections import deque
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent

# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

# backtrack to find the path from start to goal by repeatedly retrieving parents
def backchain(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path

# breadth-first search
def bfs_search(search_problem):
    solution = SearchSolution(search_problem, "BFS") # initialize SearchSolution

    frontier = deque() # frontier = new queue
    start_state = search_problem.start_state # retrieve start state
    start_node = SearchNode(start_state) # pack start state into a node
    frontier.append(start_node) # add node to frontier

    explored = set() # explored = new set
    explored.add(start_state) # add start_state to explored

    while frontier: # while frontier is not empty
        current_node = frontier.popleft() # get current_node from the frontier
        solution.nodes_visited += 1 # increment nodes visited
        current_state = current_node.state # get current_state from current_node

        if search_problem.goal_test(current_state): # if current_state is the goal
            # backchain from current_node and return solution
            solution.path = backchain(current_node) 
            return solution

        children = search_problem.get_successors(current_state)
        for child_state in children: # for each child of current_state
            if child_state not in explored: # if child not in explored
                explored.add(child_state) # add child to explored
                child_node = SearchNode(child_state, current_node) # pack child state into a node, with backpointer to current_node
                frontier.append(child_node) # add the node to the frontier

    return solution # return failure

# path-checking depth-first search
# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # you write this part
    solution.nodes_visited += 1 # another node got visited
    state = node.state # retrieve its state

    if state in solution.path: # Base case 1: if state already in path, skip so doesn't loop
        return solution
    
    solution.path.append(state) # add state to path

    if search_problem.goal_test(state): # Base case 2: if state is goal, return solution
        return solution

    if depth_limit < 0: # Base case 3: depth limit crossed, remove that node and return failure
        solution.path.pop()
        return solution
    
    children = search_problem.get_successors(state) # retrieve its children
    for child_state in children: # for each child of current_state
        if child_state in solution.path: # if its already in path, skip so doesn't loop
            continue
        child_node = SearchNode(child_state, node) # pack child state into node, add backpointer
        found = dfs_search(search_problem, depth_limit=depth_limit - 1, node=child_node, solution=solution) # recurse search on that node
        if search_problem.goal_state in found.path: # if goal found, return solution
            return found
    
    solution.path.pop() # if gone through all children of that node and found no goal, remove that node from the path
    return solution # return failure

# iterative deepening search
def ids_search(search_problem, depth_limit=100):
    # you write this part
    depth = 0
    node = SearchNode(search_problem.start_state) # initialize start node
    solution = SearchSolution(search_problem, "IDS") # initialize SearchSolution

    while depth <= depth_limit:
        found = dfs_search(search_problem, depth_limit=depth, node=node, solution=solution) # run path-checking dfs on depth limit starting from 0
        if search_problem.goal_state in found.path: # if found goal
            solution.path, solution.nodes_visited = found.path, found.nodes_visited # update solution
            return solution # return solution
        depth += 1 # increment depth limit if goal has not been found
    return solution # return failure