def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    arrL = arr[:mid]
    arrR = arr[mid:]
    mergeSort(arrL)
    mergeSort(arrR)
    merge(arrL, arrR, arr)
    return arr
def merge(arrL, arrR, arr):
    i = j = k = 0
    while i < len(arrL) and j < len(arrR):
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1
        k += 1
    while i < len(arrL):
        arr[k] = arrL[i]
        k += 1
        i += 1
    while j < len(arrR):
        arr[k] = arrR[j]
        k += 1
        j += 1
newArr = [6, 2, 6, 15, 7, 8, 3]
print(newArr)
mergeSort(newArr)
print(newArr)