n, m, s, d, k = map(int, input().split())
g = []
for i in range(n + 1):
    g += [[]]
for i in range(m):
    u, v = map(int, input().split())
    g[u] += [v]
for i in range(1, n + 1):
    g[i].sort()
def bfs(x):
    vis = [False] * (n + 1)
    par = [-1] * (n + 1)
    q = [x]
    vis[x] = True
    c = 0
    while c < len(q):
        u = q[c]
        c += 1
        for i in g[u]:
            if vis[i] == False:
                vis[i] = True
                par[i] = u
                q += [i]
    return par
p1 = bfs(s)
p2 = bfs(k)
if (p1[k] == -1 and s != k) or (p2[d] == -1 and k != d):
    print(-1)
else:
    temp1 = []
    x = k
    while x != -1:
        temp1 += [x]
        x = p1[x]
    temp1 = temp1[::-1]
    temp2 = []
    x = d
    while x != -1 and x != k:
        temp2 += [x]
        x = p2[x]
    if x == k:
        temp2 += [k]
        temp2 = temp2[::-1]
        ans = temp1[:-1] + temp2
        print(len(ans) - 1)
        print(*ans)
    else:
        print(-1)