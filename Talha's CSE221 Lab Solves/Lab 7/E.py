import heapq
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
INF = float('inf')
adj = []
dist = []
q = []
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    adj[u[i]] += [(v[i], w[i])]
for i in range(N + 1):
    dist += [[INF, INF]]
for x, y in adj[1]:
    z = y % 2
    if y < dist[x][z]:
        dist[x][z] = y
        heapq.heappush(q, (y, x, z))
while q:
    a, b, c = heapq.heappop(q)
    if a > dist[b][c]:
        continue
    for i, j in adj[b]:
        d = j % 2
        if d == c:
            continue
        e = a + j
        if e < dist[i][d]:
            dist[i][d] = e
            heapq.heappush(q, (e, i, d))
ans = min(dist[N][0], dist[N][1])
if ans == INF:
    print(-1)
else:
    print(ans)