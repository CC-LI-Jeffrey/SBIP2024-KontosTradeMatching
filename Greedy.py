def findmin(mt, n, c, z1, z2, v):
    m = mt
    cost = 0
    l = list(range(n))
    l.sort(key=lambda element: z1[element])
    i = 0
    while m > 0 and i < n:
        cost += z1[i]
        for j in range(c[i]):
            if m >= v[i][j]:
                m -= v[i][j]
                cost += z2[i]
            else:
                break
        i += 1
    return cost
