# Function to detect negative weight cycle using Floyd-Warshall Algorithm
def detect_negative_cycle(graph, V):
    # Initialize the distance matrix with graph values
    dist = [[float('inf')] * V for _ in range(V)]
    
    # Copy the graph to dist array
    for u in range(V):
        for v in range(V):
            dist[u][v] = graph[u][v]
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Check for negative weight cycle
    for i in range(V):
        if dist[i][i] < 0:  # If distance to self is negative, a negative cycle exists
            return True

    return False

# Example usage
V = 4
graph = [[0, 1, float('inf'), float('inf')],
         [float('inf'), 0, -1, float('inf')],
         [float('inf'), float('inf'), 0, -1],
         [-1, float('inf'), float('inf'), 0]]

if detect_negative_cycle(graph, V):
    print("Negative weight cycle detected")
else:
    print("No negative weight cycle detected")
