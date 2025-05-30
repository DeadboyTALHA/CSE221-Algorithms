n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
g = []
vis = [False] * (n + 1)
p = [-1] * (n + 1)
q = [s]
vis[s] = True
c = 0
for i in range(n + 1):
    g += [[]]
for i in range(m):
    g[u[i]] += [v[i]]
    g[v[i]] += [u[i]]
for i in range(1, n + 1):
    g[i].sort()
while c < len(q):
    node = q[c]
    c += 1
    for i in g[node]:
        if vis[i] == False:
            vis[i] = True
            p[i] = node
            q += [i]
if vis[d] == True:
    ans = []
    while d != -1:
        ans += [d]
        d = p[d]
    print(len(ans) - 1)
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=' ')
else:
    print(-1)