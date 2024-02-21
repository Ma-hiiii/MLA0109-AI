import heapq

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def actions(self):
        empty_row, empty_col = self.state.index(0) // 3, self.state.index(0) % 3
        for dr, dc, action in [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]:
            new_row, new_col = empty_row + dr, empty_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = list(self.state)
                new_state[empty_row * 3 + empty_col], new_state[new_row * 3 + new_col] = new_state[new_row * 3 + new_col], new_state[empty_row * 3 + empty_col]
                yield (action, new_state)

    def is_goal(self):
        return self.state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def manhattan_distance(self):
        distance = 0
        for i in range(9):
            if self.state[i] != 0:
                distance += abs(i // 3 - (self.state[i] - 1) // 3) + abs(i % 3 - (self.state[i] - 1) % 3)
        return distance

    def heuristic(self):
        return self.manhattan_distance() + self.depth

def a_star_search(initial_state):
    frontier = []
    heapq.heappush(frontier, Node(initial_state))
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.is_goal():
            return node
        explored.add(node)
        for action, new_state in node.actions():
            child = Node(new_state, node, action, node.depth + 1, node.depth + 1 + new_state.index(0))
            if child not in explored:
                heapq.heappush(frontier, child)

    return None

def print_solution(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()
    for i, state in enumerate(path):
        print(f'Step {i}: {state.action if state.action else "Initial State"}')
        print(state)

initial_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
solution = a_star_search(initial_state)
print_solution(solution)
