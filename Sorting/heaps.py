def heapify(arr, n, index):
    indexC = index - 1
    largest = indexC
    left = 2 * indexC + 1
    right = 2 * indexC + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != indexC:
        arr[indexC], arr[largest] = arr[largest], arr[indexC]
        heapify(arr, n, largest + 1)

A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
print(f"Before heapify(A, 1) operation: {A}")
heapify(A, len(A), 2)
print(f"After heapify(A, 1) operation: {A}")

def constructHeap(arr, n):
    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)

print(f"Before heap construction: {A}")
constructHeap(A, len(A))
print(f"After heap construction: {A}")

def heapSort(arr):
    n = len(arr)
    constructHeap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 1)
    
print(f"Before sorting: {A}")
heapSort(A)
print(f"After heap sort: {A}")