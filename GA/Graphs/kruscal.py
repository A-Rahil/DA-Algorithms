class KruscalAlgorithm:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.edgeList = []

    def addEdge(self, u, v, weight):
        self.edgeList.append([weight, u, v])

    def find(self, parentArr, node):
        if parentArr[node] == node:
            return node
        return self.find(parentArr, parentArr[node])
    
    def union(self, parentArr, rankArr, node1, node2):
        root1 = self.find(parentArr, node1)
        root2 = self.find(parentArr, node2)
        if rankArr[root1] < rankArr[root2]:
            parentArr[root1] = root2
        elif rankArr[root1] > rankArr[root2]:
            parentArr[root2] = root1
        else:
            parentArr[root2] = root1
            rankArr[root1] += 1
    def MSTKruscal(self):
        MST = []
        edgeIndex, edgeAccepted = 0, 0 
        self.edgeList.sort() 
        parent = []
        rank = []
        for node in range(self.numVertices):
            parent.append(node)
            rank.append(0)
        while edgeAccepted < self.numVertices - 1 and edgeIndex < len(self.edgeList):
            weight, u, v = self.edgeList[edgeIndex]
            edgeIndex += 1
            rootU = self.find(parent, u)
            rootV = self.find(parent, v)
            if rootU != rootV:
                edgeAccepted += 1
                MST.append((u, v, weight))
                self.union(parent, rank, rootU, rootV)
        totalWeight = 0
        for u, v, weight in MST:
            print(f"Edge: {u}, {v} - (Weight: {weight})")
            totalWeight += weight
        print(f"Total weight: {totalWeight}")

numNodes = 8
graph = KruscalAlgorithm(numNodes)

graph.addEdge(0, 1, 1)  
graph.addEdge(1-1, 2, 7)  
graph.addEdge(2, 3, 2)  
graph.addEdge(1, 3, 5)  
graph.addEdge(1, 4, 6)  
graph.addEdge(4, 6, 9)  
graph.addEdge(4, 5, 3)  
graph.addEdge(5, 7, 8)  
graph.addEdge(6, 7, 4)

graph.MSTKruscal()