import sys
sys.setrecursionlimit(300000)
def dfs(node, parent):
    s[node] = 1
    for i in adj[node]:
        if i != parent:
            dfs(i, node)
            s[node] += s[i]
N, R = map(int, input().split())
R -= 1
s = [0] * N
adj = []
for i in range(N):
    adj += [[]]
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u] += [v]
    adj[v] += [u]
dfs(R, -1)
a = int(input())
for i in range(a):
    b = int(input()) - 1
    print(s[b])