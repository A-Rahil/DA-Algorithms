import heapq
def Djikstra(graph, start):
    costs = {node: float('inf') for node in graph}
    visited = set()
    priorityQueue = []
    costs[start] = 0
    heapq.heappush(priorityQueue, (0, start))
    while priorityQueue:
        currentCost, node = heapq.heappop(priorityQueue)
        if node in visited:
            continue
        visited.add(node)
        for v, weight in graph[node].items():
            if v not in visited and weight + currentCost < costs[v]:
                costs[v] = weight + currentCost
                heapq.heappush(priorityQueue, (weight, v))
    return costs
    
graph = {
    's': {'d': 3, 'b': 8, 'e': 10},
    'd': {'b': 14, 's': 3},
    'b': {'a': 6, 'c': 5, 's': 8, 'd': 14}, 
    'a': {'c': 12, 'b': 6},
    'e': {'g': 15, 'c': 7, 's': 10},
    'c': {'f': 9, 'b': 5, 'a': 12, 'e': 7},
    'f': {'c': 9},
    'g': {'e': 15}
}

costs = Djikstra(graph, 's')
print(costs)