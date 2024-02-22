import heapq
class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic
def a_star_search(start_state, goal_state, heuristic_fn, actions_fn, cost_fn):
    frontier = [Node(start_state, None, None, 0, heuristic_fn(start_state, goal_state))]
    heapq.heapify(frontier)
    explored = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            path.reverse()
            return path
        explored.add(current_node.state)
        for action in actions_fn(current_node.state):
            child_state = action(current_node.state)
            child_cost = current_node.cost + cost_fn(current_node.state, child_state)
            child_heuristic = heuristic_fn(child_state, goal_state)
            if child_state not in explored:
                existing_node = next((node for node in frontier if node.state == child_state), None)
                if existing_node:
                    if child_cost + child_heuristic < existing_node.cost + existing_node.heuristic:
                        existing_node.parent = current_node
                        existing_node.action = action
                        existing_node.cost = child_cost
                else:
                    heapq.heappush(frontier, Node(child_state, current_node, action, child_cost, child_heuristic))
    return None
start_state = (0, 0)
goal_state = (4, 4)
def heuristic_fn(state, goal_state):
    return max(abs(state[0] - goal_state[0]), abs(state[1] - goal_state[1]))
def actions_fn(state):
    x, y = state
    return [
        lambda s: (x+1, y),
        lambda s: (x-1, y),
        lambda s: (x, y+1),
        lambda s: (x, y-1)
    ]
def cost_fn(state1, state2):
    return 1
path = a_star_search(start_state, goal_state, heuristic_fn, actions_fn, cost_fn)
print(path)
