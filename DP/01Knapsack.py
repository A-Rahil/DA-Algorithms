objects = {
    #benefit, weight
    1: [10, 2], 
    2: [5, 3],
    3: [15, 5],
    4: [7, 7], 
    5: [6, 1], 
    6: [18, 4], 
    7: [3, 1]
}

def tableComp(objects, capacity):
    n = len(objects)
    benefits = [0] + [val[0] for val in objects.values()]
    weights = [0] + [val[1] for val in objects.values()]
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            currWeight = weights[i]
            currBenefit = benefits[i]
            if currWeight <= j:
                incBenefit = currBenefit + table[i - 1][j - currWeight]
                excBenefit = table[i - 1][j]
                table[i][j] = max(incBenefit, excBenefit)
            else:
                table[i][j] = table[i - 1][j]
    return table
def backTrack(table, objects, capacity):
    selectedItems = []
    w = capacity
    n = len(objects)
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selectedItems.append(i)
            currItemWeight = objects[i][1]
            w -= currItemWeight
    return selectedItems

def knapsack(objects, capacity):
    table = tableComp(objects, capacity)
    selectedItems = backTrack(table, objects, capacity)
    return selectedItems

selectedItems = knapsack(objects, 10)
print(f"Selected items are: {selectedItems[::-1]}")