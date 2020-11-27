import random
def classicMul(a, b):
    if len(b) != len(a[0]):
        print("Different dimension of the matrics")
        return
    n = len(a)
    m = len(a[0])
    k = len(b[0])
    res = [[0 for i in range(0, k)] for j in range(0, n)]
    for i in range(n):
        for j in range(m):
            for t in range(k):
                res[i][t] += a[i][j] * b[j][t]
    return res
