import heapq
N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
adj = []
INF = float('inf')
dist = [INF] * (N + 1)
dist[S] = 0
p = [-1] * (N + 1)
hp = []
heapq.heappush(hp, (0, S))
for i in range(N + 1):
    adj += [[]]
for i in range(M):
    adj[u[i]] += [(v[i], w[i])]
while hp:
    d, u1 = heapq.heappop(hp)
    if d > dist[u1]:
        continue
    for x, y in adj[u1]:
        if dist[x] > dist[u1] + y:
            dist[x] = dist[u1] + y
            p[x] = u1
            heapq.heappush(hp, (dist[x], x))
if dist[D] == INF:
    print(-1)
else:
    print(dist[D])
    ans = []
    c = D
    while c != -1:
        ans += [c]
        c = p[c]
    ans.reverse()
    print(*ans)