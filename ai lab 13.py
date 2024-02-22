import random
class Problem:
    def __init__(self, initial_state_fn, value_fn, neighbors_fn):
        self.initial_state = initial_state_fn
        self.value = value_fn
        self.neighbors = neighbors_fn
def hill_climbing(problem, max_iterations=1000):
    current_state = problem.initial_state()
    current_value = problem.value(current_state)
    for _ in range(max_iterations):
        neighbors = problem.neighbors(current_state)
        if not neighbors:
            break
        next_state = max(neighbors, key=lambda state: problem.value(state))
        next_value = problem.value(next_state)
        if next_value <= current_value:
            break
        current_state = next_state
        current_value = next_value

def initial_state_fn():
    return 0

def value_fn(state):
    return -state**2

def neighbors_fn(state):
    return [state + random.choice([-1, 1])]

problem = Problem(initial_state_fn, value_fn, neighbors_fn)
solution = hill_climbing(problem)
print(solution)
