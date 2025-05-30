n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
c = [0] * (n + 1)
d = 0
for i in range(m):
    c[u[i]] += 1
    c[v[i]] += 1
for i in range(1, n + 1):
    if c[i] % 2 == 1:
        d += 1
if d == 0 or d == 2:
    print("YES")
else:
    print("NO")