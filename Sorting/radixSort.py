list = [64, 8, 216, 512, 27, 729, 0, 1, 343, 125]
def firstPass(A):
    aux = {}
    for i in range(10):
        aux[i] = []
    for i in range(len(A)):
        tens = A[i] % 10
        aux[tens].append(A[i])
    index = 0
    for digit in range(10):
        for number in aux[digit]:
            A[index] = number
            index += 1
def secondPass(A):
    aux = {}
    for i in range(10):
        aux[i] = []
    for i in range(len(A)):
        hundreds = (A[i] // 10) % 10
        aux[hundreds].append(A[i])
    index = 0
    for hundredth in range(10):
        for number in aux[hundredth]:
            A[index] = number
            index += 1
def thirdPass(A):
    aux = {}
    for i in range(10):
        aux[i] = []
    for i in range(len(A)):
        thousands = (A[i] // 100) % 10
        aux[thousands].append(A[i])
    index = 0
    for thousandth in range(10):
        for number in aux[thousandth]:
            A[index] = number
            index += 1
def radixSort(A):
    firstPass(A)
    secondPass(A)
    thirdPass(A)
radixSort(list)
print(list)