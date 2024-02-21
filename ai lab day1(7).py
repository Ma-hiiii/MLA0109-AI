from collections import deque

class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, vertex, edge):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        self.graph_dict[vertex].append(edge)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)

            for neighbour in self.graph_dict[current_vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

# Example usage:
graph = Graph({
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
})

graph.bfs('A')
