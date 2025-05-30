import heapq
N, M, S, D = map(int, input().split())
adj = []
INF = float('inf')
dist = []
q = []
heapq.heappush(q, (0, S))
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    u, v, w = map(int, input().split())
    adj[u] += [(v, w)]
    adj[v] += [(u, w)]
for i in range(N + 1):
    dist += [[INF, INF]]
dist[S][0] = 0
while q:
    a, b = heapq.heappop(q)
    for i, j in adj[b]:
        k = a + j
        if k < dist[i][0]:
            dist[i][1] = dist[i][0]
            dist[i][0] = k
            heapq.heappush(q, (k, i))
        elif dist[i][0] < k < dist[i][1]:
            dist[i][1] = k
            heapq.heappush(q, (k, i))
if dist[D][1] == INF:
    print(-1)
else:
    print(dist[D][1])