def getSmallest(arr):
    smallest = arr[0]
    idx = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            idx = i
    return smallest, idx
def insertionSort(arr):
    sortedArr = []
    for i in range(len(arr)):
        smallest, idx = getSmallest(arr)
        sortedArr.append(smallest)
        arr.pop(idx)
    return sortedArr
myList = [9, 3, 15, 27, 1, 6]
print(f"Befire sorting: {myList}")
print(f"After sorting: {insertionSort(myList)}")