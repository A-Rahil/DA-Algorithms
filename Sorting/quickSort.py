def QSort(arr, f, e):
    if (f >= e):
        return 
    pivot = partition(arr, f, e)
    QSort(arr, f, pivot - 1)
    QSort(arr, pivot + 1, e)
def partition(arr, f, e):
    pivot = arr[e]
    i = f - 1
    for j in range(f, e):
        if (arr[j] < pivot):
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    temp = arr[i]
    arr[i] = arr[e]
    arr[e] = temp
    return i    

arr = [5, 4, 8, 6, 7, 5, 4, 8, 6, 7]
print(arr)
QSort(arr, 0, 8)
print(arr)

def removeDuplicates(arr):
    index = 0
    B = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            index += 1
            B.append(arr[index])
    return B
removeDuplicates(arr)
print(arr)