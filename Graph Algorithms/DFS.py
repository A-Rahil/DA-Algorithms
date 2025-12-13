def DFS(start, graph, visited):
    neighbors = graph[start]
    visited.append(start)
    print(f"Visited {start}")
    for neighbor in neighbors:
        if neighbor not in visited:
            DFS(neighbor, graph, visited)
graph = {
    'v': ['r'],
    'r': ['v', 's'],
    's': ['w', 'r'],
    'w': ['t', 'x', 's'],
    't': ['u', 'x', 'w'],
    'x': ['w', 'y', 't'],
    'y': ['u', 'x'],
    'u': ['t', 'y']
}
visited = []
DFS('v', graph, visited)