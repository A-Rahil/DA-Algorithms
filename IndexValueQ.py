## Given a sorted array of distinct integers A[1,...,n], you want to find out whether there is an
## index i for which A[i] = i. Give a divide-and-conquer algorithm that runs in time O(logn)

def IndexValue(arr, low, high):
    if low >= high:
        return False
    mid = (low + high) // 2
    if arr[mid] == mid:
        return True
    elif arr[mid] > mid:
        return IndexValue(arr, low, mid - 1)
    else:
        return IndexValue(arr, mid + 1, high)