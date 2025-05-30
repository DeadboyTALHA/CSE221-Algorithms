from collections import deque
def bfs(s, n, adj):
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    x = s
    y = 0
    while len(q) != 0:
        node = q.popleft()
        for i in adj[node]:
            if dist[i] == -1:
                dist[i] = dist[node] + 1
                q += [i]
                if dist[i] > y:
                    x = i
                    y = dist[i]
    return x, y
N = int(input())
adj = []
for i in range(N):
    adj += [[]]
for i in range(N - 1):
    u, v = map(int, input().split())
    adj[u-1] += [v-1]
    adj[v-1] += [u-1]
a, b = bfs(0, N, adj)
c, d = bfs(a, N, adj)
print(d)
print(a + 1, c + 1)