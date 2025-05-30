n, m = map(int, input().split())
adj = []
ind = [0] * (n + 1)
ans = []
q = []
c = 0
for i in range(n + 1):
    adj += [[]]
for i in range(m):
    a, b = map(int, input().split())
    adj[a] += [b]
    ind[b] += 1
for i in range(1, n + 1):
    if ind[i] == 0:
        q += [i]
while c < len(q):
    x= q[c]
    c += 1
    ans += [x]
    for i in adj[x]:
        ind[i] -= 1
        if ind[i] == 0:
            q += [i]
if len(ans) == n:
    print(*ans)
else:
    print(-1)