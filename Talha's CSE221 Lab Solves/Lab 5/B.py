import sys
sys.setrecursionlimit(2 * 100000 + 5)
n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
g = []
vis = [False] * (n + 1)
ans = []
for i in range(n + 1):
    g += [[]]
for i in range(m):
    g[u[i]] += [v[i]]
    g[v[i]] += [u[i]]
for i in range(1, n + 1):
    g[i].sort()
def dfs(node):
    vis[node] = True
    ans.append(node)
    for i in g[node]:
        if vis[i] == False:
            dfs(i)
dfs(1)
print(*ans)