import heapq
N, M = map(int, input().split())
adj = []
INF = float('inf')
d = [INF] * (N + 1)
d[1] = 0
q = [(0, 1)]
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    u, v, w = map(int, input().split())
    adj[u] += [(v, w)]
    adj[v] += [(u, w)]
while q:
    x, y = heapq.heappop(q)
    if x > d[y]:
        continue
    for i, j in adj[y]:
        z = max(x, j)
        if z < d[i]:
            d[i] = z
            heapq.heappush(q, (z, i))
for i in range(1, N + 1):
    if d[i] == INF:
        print(-1, end=" ")
    else:
        print(d[i], end=" ")