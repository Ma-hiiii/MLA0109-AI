class Game:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def utility(self, state, player):
        raise NotImplementedError

    def terminal_test(self, state):
        return not self.actions(state)

class TicTacToe(Game):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def actions(self, state):
        return [(i, j) for i in range(3) for j in range(3) if state[i][j] == " "]

    def result(self, state, action):
        i, j = action
        player = "X" if sum(row.count("X") for row in state) == sum(row.count("O") for row in state) else "O"
        new_state = [row.copy() for row in state]
        new_state[i][j] = player
        return new_state

    def utility(self, state, player):
        if any(all(cell == player for cell in row) for row in state):
            return 1 if player == "X" else -1
        if all(cell != " " for row in state for cell in row):
            return 0
        return None

def minimax(game, state):
    def max_value(state):
        if game.terminal_test(state):
            return game.utility(state, "X")
        v = float('-inf')
        for action in game.actions(state):
            v = max(v, min_value(game.result(state, action)))
        return v

    def min_value(state):
        if game.terminal_test(state):
            return game.utility(state, "O")
        v = float('inf')
        for action in game.actions(state):
            v = min(v, max_value(game.result(state, action)))
        return v

    return max(game.actions(state), key=lambda action: min_value(game.result(state, action)))

# Example usage
initial_state = [[" " for _ in range(3)] for _ in range(3)]
game = TicTacToe(initial_state)
print(minimax(game, initial_state))
