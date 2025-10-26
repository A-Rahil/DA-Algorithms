def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    #The function modifies the array, so I don't need to return anything
numArr = [12, 6, 15, 9, 7, 13, 14, 20]
print(numArr)
InsertionSort(numArr)
print(numArr) 