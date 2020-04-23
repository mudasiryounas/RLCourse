import numpy as np


class Agent:
    def __init__(self):
        self.epsilon = 0.1  # based on this probability we will be choosing b/w exploration or exploitation, ie choosing a random action or take a greedy action
        self.alpha = 0.5  # learning rate, will be used in our value function todo write this function in document
        self.verbose = False  # todo ????
        self.state_history = []  # this will be our history which will keep all the states

    def set_value_function(self, V):
        self.V = V

    def set_symbol(self, symbol):
        self.symbol = symbol

    def reset_history(self):
        self.state_history = []

    def choose_random_action(self, env):
        print("Taking random action...")
        empty_moves = env.get_empty_moves()
        # select randomly from possible moves
        # this will generate any random integer based on given possible moves e.g lts say there are 3 possible moves so it will give us 0, 1 or 2
        random_index_from_empty_moves = np.random.choice(len(empty_moves))
        next_random_move = empty_moves[random_index_from_empty_moves]
        return next_random_move

    def choose_best_action_from_states(self, env):
        print("Taking best action...")
        next_best_move, best_state = env.get_next_best_move()
        return next_best_move, best_state

    def get_next_move(self, env):
        next_best_move, best_state = None, None
        # first of all we choose an action based on epsilon greedy strategy,
        # which will decide weather to take any random action or select from history
        random_number = np.random.rand()  # will give a random float between 0 and 1
        if random_number < self.epsilon:
            # take a random action
            next_move = self.choose_random_action(env)
        else:
            # choose the best action based on current values of states, loop through all values and select the best one
            next_best_move, best_state = self.choose_best_action_from_states(env)
        return next_best_move, best_state

    def take_action(self, env):
        selected_next_move, best_state = self.get_next_move(env)

        # make next move
        env.board[selected_next_move[0], selected_next_move[1]] = self.symbol

    # this function is used to append each state to state_history, in order to utilise later
    def update_state_history(self, state):
        self.state_history.append(state)

    def update(self, env):
        # we will only update at the end of an episode
        # we will backtrack over all the states to collect function value
        # V(prev_state) = V(prev_state) + alpha * ( V(next_state) - V(pre_state) ), where V(next_state) is reward if its most current state

        reward = env.reward(self.symbol)
        target = reward
        for prev in reversed(self.state_history):
            value = self.V[prev] + self.alpha * (target - self.V[prev])
            self.V[prev] = value
            target = value
        self.reset_history()


class Environment:

    def __init__(self):
        self.board = np.zeros((3, 3))  # make an 2D array with zeros, zero means the box is empty
        self.x = -1  # player 1
        self.o = 1  # player 2
        self.winner = None  # initially there is no winner
        self.ended = False  # game is not ended initially
        self.max_states = 3 ** (3 * 3)  # =19683, total number of possible states for tic tac toe game

    def is_empty(self, i, j):
        # this will tell us if (i, j) position on board is empty or not
        return self.board[i, j] == 0

    def reward(self, symbol):
        # we will not give any reward until game is over, so at the end of an game agent will get reward for this game
        collected_reward = 0
        if self.game_over() and self.winner == symbol:  # if game is over and winner is this symbol that is this player then we give 1 as a reward to this player
            collected_reward = 1
        return collected_reward

    def is_draw(self):
        is_draw = False
        if self.ended and self.winner is None:  # if game is ended and there is not winner so we consider is as draw game
            is_draw = True
        return is_draw

    def game_over(self):
        is_game_over = False
        # returns True if any player has won or game is drwa
        if self.ended:  # return True if this environment has ended ie if this game has ended
            return True  # game is over

        # now we will check if there is any sequence of same symbols for any player ie if any player has won the game todo explain this on article with images

        players = [self.x, self.o]

        # check if there are any same symbols on rows side
        for i in range(3):
            for player in players:
                if self.board[i].sum() == player * 3:  # results will be  1+1+1 = 3 for player o and -1-1-1 = -3 for player x
                    self.winner = player
                    self.ended = True
                    return True  # game is over

        # check if there are any same symbols on columns side
        for j in range(3):
            for player in players:
                if self.board[:, j].sum() == player * 3:
                    self.winner = player
                    self.ended = True
                    return True  # game is over

        # finally if there is no same symbols on either rows or columns we check on diagonal sides
        for player in players:
            # top-left -> bottom-right diagonal
            # trace() function Return the sum along diagonals of the array
            if self.board.trace() == player * 3:
                self.winner = player
                self.ended = True
                return True  # game is over

        # now that we have checked all the winning conditions and still if there is no winner we check for draw
        # np.all() function Test whether all array elements along a given axis evaluate to True.
        if np.all((self.board == 0) == False):  # check if all axis sum is not equal to zero todo ????
            # game is draw hence there is no winner
            self.winner = None
            self.ended = True
            return True  # game is over

        # finally if game is not over
        self.winner = None
        return False

    def get_state(self):
        pass

    def get_empty_moves(self):
        empty_moves = []
        # we will be looping to all 9 boxes, and collecting possible moves which are empty
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):  # check if this box is empty or not
                    empty_moves.append((i, j))
        return empty_moves

    def get_next_best_move(self, agent):
        # symbol will be X or O
        # we will loop to all empty moves and select with best value
        best_value = -1  # lets initialize with something lower
        next_best_move = None
        best_state = None
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    # lets amke this move and check what will be the state if we choose this move ie, (i, j) move, we we will revert it back after getting state
                    self.board[i, j] = agent.symbol
                    state = self.get_state()
                    self.board[i, j] = 0  # revert back to empty state ie actual state
                    if agent.V[state] > best_value:
                        best_value = agent.V[state]
                        best_state = state
                        next_best_move = (i, j)

        return next_best_move, best_state
