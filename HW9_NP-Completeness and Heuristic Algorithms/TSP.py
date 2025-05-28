def solve_tsp(G):
    """Solves the Traveling Salesman Problem using the Nearest-Neighbor heuristic"""
    num = len(G)  # Number of cities
    visited = [False] * num  # Track visited nodes
    path = [0]  # Start from node 0
    visited[0] = True
    curr = 0  # Start at node 0

    for i in range(num - 1):
        nearest_neighbor = None
        min_distance = float('inf')

        for neighbor in range(num):
            if not visited[neighbor] and G[curr][neighbor] > 0:
                if G[curr][neighbor] < min_distance:
                    min_distance = G[curr][neighbor]
                    nearest_neighbor = neighbor

        if nearest_neighbor is not None:
            path.append(nearest_neighbor)
            visited[nearest_neighbor] = True
            curr = nearest_neighbor

    path.append(0)  # Return to the starting node
    return path


# Example usage
G = [
    [0, 2, 3, 20, 1],
    [2, 0, 15, 2, 20],
    [3, 15, 0, 20, 13],
    [20, 2, 20, 0, 9],
    [1, 20, 13, 9, 0],
]

print(solve_tsp(G))