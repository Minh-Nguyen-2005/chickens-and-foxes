# Author: Minh Nguyen, Date: 10/02/2025

class FoxProblem:
    # a search problem includes start state and goal state
    def __init__(self, start_state=(3, 3, 1)):
        # state = (chickens, foxes, boats)
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        # you might want to add other things to the problem,
        #  like the total number of chickens and foxes (which you can figure out
        #  based on start_state
        self.total_chicken = start_state[0]
        self.total_fox = start_state[1]

    # check if a state is legal
    def state_safe(self, state):
        (chicken, fox, boat) = state # get the number of chickens, foxes, and boats on the river bank
        other_chicken = self.total_chicken - chicken # number of chickens on the other bank
        other_fox = self.total_fox - fox # number of foxes on the other bank

        if boat not in (0, 1): # there can only be none or one boat on the bank
            return False
        if chicken < fox and chicken > 0: # if theres chickens on the bank, cannot be less than foxes
            return False
        if other_chicken < other_fox and other_chicken > 0: # if theres chickens on the other bank, cannot be less than foxes
            return False
        if not (0 <= chicken <= self.total_chicken): # check for invalid number of chickens
            return False
        if not (0 <= fox <= self.total_fox): # check for invalid number of foxes
            return False
        
        return True
    
    # get successor states for the given state
    def get_successors(self, state):
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        successors = [] # successors list
        (chickens, foxes, boats) = state # retrieve number of chickens, foxes, and boats
        possible_moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)] # set of legal actions (boat can carry 1 or 2 animals only)

        for (c, f) in possible_moves: # loop through every moves
            if boats == 1: # if theres a boat starting from the bank, then it should carry chickens and foxes away
                if self.state_safe((chickens - c, foxes - f, boats - 1)): # if action is legal, add to successors list
                    successors.append((chickens - c, foxes - f, boats - 1))
            else: # boats == 0, if the boat is on the other side, then it should bring chickens and foxes to the bank
                if self.state_safe((chickens + c, foxes + f, boats + 1)): # if action is legal, add to successors list
                    successors.append((chickens + c, foxes + f, boats + 1))
                    
        return successors
    
    # I also had a goal test method. You should write one.
    def goal_test(self, state):
        if state == self.goal_state: # check if state is goal
            return True
        return False

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
