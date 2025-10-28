#This was done just for a HW question to learn how partitioning would work for an array with equal elements

def QSort(arr):
    if len(arr) < 2:
        return arr
    greater = []
    lesser = []
    pivot = arr[len(arr) // 2]
    for i in arr:
        if i <= pivot:
            lesser.append(i)
        elif i >= pivot:
            greater.append(i)
    return lesser, pivot, greater

elems = [2, 2, 2, 2, 2, 2, 2, 2, 2]
less, piv, great = QSort(elems)
print(f"This is less than: {less}")
print(f"This is pivot: {piv}")
print(f"This is greater than: {great}")