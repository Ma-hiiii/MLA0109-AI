class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __eq__(self, other):
        return (self.missionaries, self.cannibals, self.boat) == (other.missionaries, other.cannibals, other.boat)

    def __str__(self):
        return f'M: {self.missionaries}, C: {self.cannibals}, B: {self.boat}'

def is_valid_state(state):
    return state.missionaries >= 0 and state.cannibals >= 0 and state.missionaries <= 3 and state.cannibals <= 3 and (state.missionaries == 0 or state.missionaries >= state.cannibals)

def get_next_states(state):
    next_states = []
    if state.boat == 'left':
        next_states.append(State(state.missionaries - 2, state.cannibals, 'right'))
        next_states.append(State(state.missionaries - 1, state.cannibals - 1, 'right'))
        next_states.append(State(state.missionaries, state.cannibals - 2, 'right'))
        next_states.append(State(state.missionaries - 1, state.cannibals, 'right'))
        next_states.append(State(state.missionaries, state.cannibals - 1, 'right'))
    else:
        next_states.append(State(state.missionaries + 2, state.cannibals, 'left'))
        next_states.append(State(state.missionaries + 1, state.cannibals + 1, 'left'))
        next_states.append(State(state.missionaries, state.cannibals + 2, 'left'))
        next_states.append(State(state.missionaries + 1, state.cannibals, 'left'))
        next_states.append(State(state.missionaries, state.cannibals + 1, 'left'))
    return [s for s in next_states if is_valid_state(s)]

def solve():
    initial_state = State(3, 3, 'left')
    queue = [initial_state]
    visited = set()

    while queue:
        current_state = queue.pop(0)

        if current_state.missionaries == 0 and current_state.cannibals == 0 and current_state.boat == 'right':
            return True

        visited.add(current_state)

        next_states = get_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)

    return False

if solve():
    print("Solution found.")
else:
    print("No solution found.")
