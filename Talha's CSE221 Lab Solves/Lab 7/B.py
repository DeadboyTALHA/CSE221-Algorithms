import heapq
N, M, S, T = map(int, input().split())
adj = []
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    u, v, w = map(int, input().split())
    adj[u] += [(v, w)]
def dijkstra(s, N, adj):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[s] = 0
    hp = [(0, s)]
    while hp:
        d, u = heapq.heappop(hp)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(hp, (dist[v], v))
    return dist
dist1 = dijkstra(S, N, adj)
distB = dijkstra(T, N, adj)
INF = float('inf')
t1 = INF
node = -1
for i in range(1, N + 1):
    if dist1[i] != INF and distB[i] != INF:
        t2 = max(dist1[i], distB[i])
        if t2 < t1 or (t2 == t1 and i < node):
            t1 = t2
            node = i
if node == -1:
    print(-1)
else:
    print(t1, node)