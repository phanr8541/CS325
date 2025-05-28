import heapq


def Prims(G):
    # Number of vertices in the graph
    n = len(G)

    # Priority queue to store the edges in the form of (weight, vertex1, vertex2)
    min_heap = []

    # List to track the vertices included in the MST
    in_mst = [False] * n

    # Start from the 0th vertex
    in_mst[0] = True

    # Add all edges from the starting vertex (0) to the heap
    for i in range(1, n):
        if G[0][i] > 0:
            heapq.heappush(min_heap, (G[0][i], 0, i))

    mst_edges = []

    # While the heap is not empty
    while min_heap:
        # Pop the edge with the minimum weight
        weight, u, v = heapq.heappop(min_heap)

        # If the vertex 'v' is not yet included in the MST
        if not in_mst[v]:
            # Add the edge to the MST
            mst_edges.append((u, v, weight))
            in_mst[v] = True

            # Add all the edges from vertex 'v' to the heap
            for i in range(n):
                if not in_mst[i] and G[v][i] > 0:
                    heapq.heappush(min_heap, (G[v][i], v, i))

    return mst_edges
