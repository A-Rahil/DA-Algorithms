def bellmanFord(src, graph):
    iter = len(graph)
    costs = {node: float('inf') for node in graph}
    costs[src] = 0
    for i in range(iter - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if costs[u] + weight < costs[v]:
                    costs[v] = costs[u] + weight
    for u in graph:
            for v, weight in graph[u].items():
                if costs[u] + weight < costs[v]:
                    print("Negative cycle in the graph")
                    return None
    return costs
graph = {
    's': {'d': 3, 'b': 8, 'e': 10},
    'd': {'b': 14, 's': 3},
    'b': {'a': 6, 'c': -5, 's': 8, 'd': 14}, 
    'a': {'c': 12, 'b': 6},
    'e': {'g': 15, 'c': 7, 's': 10},
    'c': {'a': 12, 'e': 7},
    'f': {'c': -4},
    'g': {'e': 15, 'f': 6}
}

costs = bellmanFord('s', graph)
print(costs)