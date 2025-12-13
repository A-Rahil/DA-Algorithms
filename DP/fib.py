def fibComp(n):
    fib = [0] * n
    fib[0], fib[1] = 0, 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib
print(fibComp(5))