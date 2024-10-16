import sys

def bellman_ford(graph, source):
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0

    s = 1
    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        s = 0
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
                    s = 1

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return None, None  # Negative cycle detected

    return distances, predecessors


# Example graph with 9 nodes and a negative cycle
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3},
    'F': {'E': -1},
    'G': {'F': -1},
    'H': {'G': -1},
    'I': {'H': -1, 'A': -1}
}

print(bellman_ford(graph, "B"))