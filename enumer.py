def find_min_cost(mt, n, oc, oz1, oz2_values, ov):
    INF = int(1e18)
    c = [0] * n
    v = [[0] * 15 for _ in range(n)]
    z1 = [0] * n
    z2 = [0] * n
    a = []
    b = []
    prefix_min_cost_idx = []
    min_cost = INF

    oz2 = [(oz2_values[i], i) for i in range(n)]
    oz2.sort()

    for i in range(n):
        idx = oz2[i][1]
        c[i], z1[i], z2[i] = oc[idx], oz1[idx], oz2[i][0]
        v[i][:c[i]] = ov[idx][:c[i]]

    for i in range(n):
        v[i][:c[i]] = sorted(v[i][:c[i]], reverse=True)

    cn1 = n // 2 if n % 2 == 0 else n // 2 + 1

    def enumerate_combinations(value, cost, next_val, i, i2):
        nonlocal min_cost
        if value >= mt:
            min_cost = min(min_cost, cost)
            return
        if i == i2:
            (a if i2 == cn1 else b).append((value, cost))
            return

        for j in range(c[i] + 1):
            if j > 0 and v[i][j - 1] <= next_val:
                break
            prev_value, prev_cost = value, cost
            for k in range(j):
                value += v[i][k] - z2[i]
                cost += z2[i]
            if j:
                value -= z1[i]
                cost += z1[i]

            enumerate_combinations(value, cost, v[i][j] if j < c[i] - 1 else 0, i + 1, i2)

            value, cost = prev_value, prev_cost

    enumerate_combinations(0, 0, 0, 0, cn1)
    enumerate_combinations(0, 0, 0, cn1, n)

    b.sort(reverse=True)
    prefix_min_cost_idx.append(0)
    for i in range(1, len(b)):
        prefix_min_cost_idx.append(i if b[i][1] < b[prefix_min_cost_idx[i - 1]][1] else prefix_min_cost_idx[i - 1])

    for i, (a_value, a_cost) in enumerate(a):
        idx = next((j for j in reversed(range(len(b))) if b[j][0] >= mt - a_value), -1)
        if idx != -1:
            combined_cost = a_cost + b[prefix_min_cost_idx[idx]][1]
            if combined_cost < min_cost and a_value + b[prefix_min_cost_idx[idx]][0] >= mt:
                min_cost = combined_cost

    return min_cost if min_cost != INF else 0
