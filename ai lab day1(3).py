from collections import deque

class State:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

    def __eq__(self, other):
        return (self.jug1, self.jug2) == (other.jug1, other.jug2)

    def __str__(self):
        return f'({self.jug1}, {self.jug2})'

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    initial_state = State(0, 0)
    queue = deque([initial_state])
    visited = set()

    while queue:
        current_state = queue.popleft()

        if current_state.jug1 == target or current_state.jug2 == target:
            return current_state

        visited.add(current_state)

        # Fill jug1
        next_state = State(jug1_capacity, current_state.jug2)
        if next_state not in visited:
            queue.append(next_state)

        # Fill jug2
        next_state = State(current_state.jug1, jug2_capacity)
        if next_state not in visited:
            queue.append(next_state)

        # Empty jug1
        next_state = State(0, current_state.jug2)
        if next_state not in visited:
            queue.append(next_state)

        # Empty jug2
        next_state = State(current_state.jug1, 0)
        if next_state not in visited:
            queue.append(next_state)

        # Pour from jug1 to jug2
        pour_amount = min(current_state.jug1, jug2_capacity - current_state.jug2)
        next_state = State(current_state.jug1 - pour_amount, current_state.jug2 + pour_amount)
        if next_state not in visited:
            queue.append(next_state)

        # Pour from jug2 to jug1
        pour_amount = min(current_state.jug2, jug1_capacity - current_state.jug1)
        next_state = State(current_state.jug1 + pour_amount, current_state.jug2 - pour_amount)
        if next_state not in visited:
            queue.append(next_state)

    return None

jug1_capacity = 4
jug2_capacity = 3
target = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target)
if solution:
    print(f"Solution found: {solution}")
else:
    print("No solution found.")
