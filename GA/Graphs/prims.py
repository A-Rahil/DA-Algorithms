import heapq
def prims(graph, start):
    mst = {node: None for node in graph}
    costs = {node: float('inf') for node in graph}
    visited = set()
    priorityQueue = []
    costs[start] = 0
    heapq.heappush(priorityQueue, (0, start))
    totalCost = 0
    while priorityQueue:
        currentCost, node = heapq.heappop(priorityQueue)
        if node in visited:
            continue
        visited.add(node)
        totalCost += currentCost
        parent = mst[node]
        for v, weight in graph[node].items():
            if v not in visited and weight < costs[v]:
                costs[v] = weight
                mst[v] = node
                heapq.heappush(priorityQueue, (weight, v))
    return mst, totalCost

    
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

MST, cost = prims(graph, 's')
print(f"The MST is {MST} with a cost of {cost}")