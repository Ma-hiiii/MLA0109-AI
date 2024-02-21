class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, vertex, edge):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        self.graph_dict[vertex].append(edge)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex)

        for neighbour in self.graph_dict[start_vertex]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

# Example usage:
graph = Graph({
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
})

graph.dfs('A')
