from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        cost, node = pq.get()
        visited.add(node)

        if node == goal:
            return True

        for neighbour, neighbour_cost in graph[node].items():
            if neighbour not in visited:
                pq.put((neighbour_cost, neighbour))

    return False

# Example usage:
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 15},
    'C': {'A': 10, 'D': 20},
    'D': {'B': 15, 'C': 20}
}

start = 'A'
goal = 'D'

result = best_first_search(graph, start, goal)
print(result)
