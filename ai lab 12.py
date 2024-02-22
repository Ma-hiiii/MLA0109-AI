class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {v: [] for v in vertices}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def color_graph(self):
        colors = {}
        for vertex in self.vertices:
            adjacent_colors = {colors[adjacent] for adjacent in self.adjacency_list[vertex] if adjacent in colors}
            for color in range(len(self.vertices)):
                if color not in adjacent_colors:
                    colors[vertex] = color
                    break
        return colors
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')]
graph = Graph(vertices)
for edge in edges:
    graph.add_edge(*edge)
colors = graph.color_graph()
print(colors)
