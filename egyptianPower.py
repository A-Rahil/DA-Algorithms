def egyptianPower(x, n):
    if n == 0:
        return 1
    else:
        half = egyptianPower(x, n // 2)
    result = half * half
    if (n % 2 == 1):
        result *= x
    return result

print(egyptianPower(2, 5)) 