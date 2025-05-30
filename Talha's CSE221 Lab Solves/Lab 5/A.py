n, m = map(int, input().split())
g = []
vis = [False] * (n + 1)
vis[1] = True
q = [1]
ans = []
c = 0
for i in range(n + 1):
    g += [[]]
for i in range(m):
    u, v = map(int, input().split())
    g[u] += [v]
    g[v] += [u]
for i in range(1, n + 1):
    g[i].sort()
while c < len(q):
    u = q[c]
    c += 1
    ans += [u]
    for v in g[u]:
        if vis[v] == False:
            vis[v] = True
            q += [v]
print(*ans)