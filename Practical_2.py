import numpy as np


inp = input().split()
n, m = int(inp[0]), int(inp[1])
qs = np.zeros((n, n), dtype=bool)

for i in range(m):
    query = input()
    query = np.array(list(query), dtype=int)
    query = np.array(query, dtype=bool)
    if not np.any(query):
        print("YES")
    else:
        for i in range(n):
            if not query[i]:
                continue
            elif not qs[i][i]:
                qs[i][i] = True
                qs[i] = query
                print("NO")
                break
            query = np.logical_xor(query, qs[i])
            if not np.any(query):
                print("YES")
                break
