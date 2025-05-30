n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
ind = [0] * (n + 1)
outd = [0] * (n + 1)
for i in range(m):
    ind[u[i]] += 1
    outd[v[i]] += 1
for i in range(1, n + 1):
    print(outd[i] - ind[i], end=' ')