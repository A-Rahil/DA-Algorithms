def LCS(X, Y):
    m, n = len(X), len(Y)
    table = [["" for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + X[i - 1]
            else:
                table[i][j] = table[i][j-1] if len(table[i][j-1]) >= len(table[i-1][j]) else table[i-1][j]
    return table[m][n]

X = 'RELATIVELY'
Y = 'ACTIVE'
print(LCS(X, Y)) 