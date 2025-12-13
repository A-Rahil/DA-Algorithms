from collections import deque
def BFS(graph, root):
    searchQueue = deque([root])
    visited = set([root])
    travOrder = []
    while searchQueue:
        currNode = searchQueue.popleft()
        travOrder.append(currNode)
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                searchQueue.append(neighbor)
    return travOrder

graph = {}
graph['v'] = ['r']
graph['r'] = ['v', 's']
graph['s'] = ['w', 'r']
graph['w'] = ['t', 'x', 's']
graph['t'] = ['u', 'x', 'w']
graph['x'] = ['w', 'y', 't']
graph['y'] = ['u', 'x']
graph['u'] = ['t', 'y']

trav = BFS(graph, 's')
print(f"This is the order of traversal: {trav}")
