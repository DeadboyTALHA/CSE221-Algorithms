n, m = map(int, input().split())
g = []
ans = 0
col = [-1] * (n + 1)
for i in range(n + 1):
    g += [[]]
for i in range(m):
    u, v = map(int, input().split())
    g[u] += [v]
    g[v] += [u]
for i in range(1, n + 1):
    if col[i] == -1:
        q = [i]
        col[i] = 0
        x = [1, 0]
        c = 0
        flag = True
        while c < len(q) and flag == True:
            y = q[c]
            c += 1
            for j in g[y]:
                if col[j] == -1:
                    col[j] = 1 - col[y]
                    x[col[j]] += 1
                    q += [j]
                elif col[j] == col[y]:
                    flag = False
                    break
        if flag == True:
            ans += max(x)
print(ans)