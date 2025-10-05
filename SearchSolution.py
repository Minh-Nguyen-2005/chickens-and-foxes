# Author: Minh Nguyen, Date: 10/02/2025

class SearchSolution: 
    # a SearchSolution contains problem name, search method used, solution path, and number of nodes visited
    def __init__(self, problem, search_method):
        self.problem_name = str(problem)
        self.search_method = search_method
        self.path = []
        self.nodes_visited = 0

    def __str__(self):
        string = "----\n"
        string += "{:s}\n"
        string += "attempted with search method {:s}\n"

        if len(self.path) > 0: # if there is a path, return solution

            string += "number of nodes visited: {:d}\n"
            string += "solution length: {:d}\n"
            string += "path: {:s}\n"

            string = string.format(self.problem_name, self.search_method,
                self.nodes_visited, len(self.path), str(self.path))
            
        else: # no path found, no solution
            string += "no solution found after visiting {:d} nodes\n"
            string = string.format(self.problem_name, self.search_method, self.nodes_visited)

        return string
