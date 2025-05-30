n, m = map(int, input().split())
e = []
p = []
c = 0
r = [0] * (n + 1)
for i in range(n + 1):
    p += [i]
for i in range(m):
    u, v, w = map(int, input().split())
    e += [(w, u, v)]
e.sort()
for w, u, v in e:
    u1 = u
    while p[u1] != u1:
        p[u1] = p[p[u1]]
        u1 = p[u1]
    v1 = v
    while p[v1] != v1:
        p[v1] = p[p[v1]]
        v1 = p[v1]
    if u1 != v1:
        if r[u1] < r[v1]:
            p[u1] = v1
        else:
            p[v1] = u1
            if r[u1] == r[v1]:
                r[u1] += 1
        c += w
print(c)