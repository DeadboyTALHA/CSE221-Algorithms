n, k = map(int, input().split())
p = []
c = [1] * (n + 1)
for i in range(n + 1):
    p += [i]
for i in range(k):
    u, v = map(int, input().split())
    u1 = u
    while p[u1] != u1:
        p[u1] = p[p[u1]]
        u1 = p[u1]
    v1 = v
    while p[v1] != v1:
        p[v1] = p[p[v1]]
        v1 = p[v1]
    if u1 != v1:
        if c[u1] < c[v1]:
            u1, v1 = v1, u1
        p[v1] = u1
        c[u1] += c[v1]
        print(c[u1])
    else:
        print(c[u1])