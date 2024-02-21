import numpy as np

# Define the function to solve the TSP using nearest neighbor algorithm
def nearest_neighbor_tsp(distances):
    n = len(distances)
    visited = [False] * n
    path = [0]
    visited[0] = True
    for _ in range(n - 1):
        current_city = path[-1]
        nearest_city = None
        nearest_distance = np.inf
        for i in range(n):
            if not visited[i] and distances[current_city][i] < nearest_distance:
                nearest_city = i
                nearest_distance = distances[current_city][i]
        path.append(nearest_city)
        visited[nearest_city] = True
    path.append(0)  
    return path

# Example usage:
cities = ['A', 'B', 'C', 'D']
distances = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

path = nearest_neighbor_tsp(distances)
print(path)
