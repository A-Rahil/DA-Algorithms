def Djikstra(graph, start):
    queue = graph.keys()
    visited = []
        

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
