def countingSort(A):
    k = findBiggest(A)
    C = [0] * (k + 1)
    B = [0] * len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, - 1, -1):
        B[C[A[i]] - 1] = A[i] 
        C[A[i]] -= 1
    return B
def findBiggest(arr):
    biggest = arr[0]
    for i in range(len(arr)):
        if arr[i] > biggest:
            biggest = arr[i]
    return biggest

arr = [4, 1, 3, 4, 3]
print(f"Before counting sort: {arr}")
print(f"After counting sort: {countingSort(arr)}")