import heapq
N, M, S, D = map(int, input().split())
w = list(map(int, input().split()))
adj = []
INF = float('inf')
dist = [INF] * (N + 1)
dist[S] = w[S - 1]
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    u, v = map(int, input().split())
    adj[u] += [v]
q = [(w[S - 1], S)]
while q:
    x, y = heapq.heappop(q)
    if x > dist[y]:
        continue
    for i in adj[y]:
        z = x + w[i - 1]
        if z < dist[i]:
            dist[i] = z
            heapq.heappush(q, (z, i))
if dist[D] == INF:
    print(-1)
else:
    print(dist[D])