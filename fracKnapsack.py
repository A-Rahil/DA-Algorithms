import heapq
objects = {
    1: [10, 2], 
    2: [5, 3],
    3: [15, 5],
    4: [7, 7], 
    5: [6, 1], 
    6: [18, 4], 
    7: [3, 1]
}

max_capacity = 15
def knapSack(objects, max_capacity):
    x = {}
    heap = []
    for i in objects:
        x[i] = 0
        v = objects[i][0] / objects[i][1]
        heapq.heappush(heap, (-v, i))   #We used a heap, negated the values because Python's heap is a min-heap. Removing an
    weightR = max_capacity              #element is logn cost , and since n removals, we are looking at nlogn complexity
    totalV = 0
    while heap and weightR > 0:
        poppedItem = heapq.heappop(heap)
        itemId = poppedItem[1]  #Getting the ID of the item
        itemValue = objects[itemId][0]
        itemWeight = objects[itemId][1]
        if weightR - itemWeight >= 0:
            x[itemId] = 1.0
            weightR -= itemWeight
            totalV += itemValue
        else:
            fraction = weightR / itemWeight
            x[itemId] = fraction
            weightR -= itemWeight * fraction
            totalV += itemValue * fraction
            break
    return totalV, x
maxValue, itemsTaken = knapSack(objects, 15)
print(f"Max value in fractional knapsack: {maxValue}")
print(f"Fractions of items taken: {itemsTaken}") 