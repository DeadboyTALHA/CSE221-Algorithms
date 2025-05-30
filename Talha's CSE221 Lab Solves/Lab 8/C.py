import sys
sys.setrecursionlimit(5000)
def f1(u, p):
    while p[u] != u:
        p[u] = p[p[u]]
        u = p[u]
    return u
def f2(u, v, p, r):
    u1 = f1(u, p)
    v1 = f1(v, p)
    if u1 == v1:
        return False
    if r[u1] < r[v1]:
        p[u1] = v1
    else:
        p[v1] = u1
        if r[u1] == r[v1]:
            r[u1] += 1
    return True
n, m = map(int, input().split())
e = []
for i in range(m):
    u, v, w = map(int, input().split())
    e += [(w, u, v)]
e.sort()
p1 = list(range(n + 1))
r1 = [0] * (n + 1)
e1 = []
c1 = 0
for w, u, v in e:
    if f2(u, v, p1, r1):
        e1 += [(w, u, v)]
        c1 += w
if len(e1) != n - 1:
    print(-1)
else:
    t = []
    for i in range(n + 1):
        t += [[]]
    for w, u, v in e1:
        t[u] += [(v, w)]
        t[v] += [(u, w)]
    p = [0] * (n + 1)
    me = [0] * (n + 1)
    d = [0] * (n + 1)
    def dfs(u, np):
        for v, w in t[u]:
            if v != np:
                p[v] = u
                me[v] = w
                d[v] = d[u] + 1
                dfs(v, u)
    dfs(1, -1)
    def get_max(u, v):
        res = 0
        while u != v:
            if d[u] < d[v]:
                res = max(res, me[v])
                v = p[v]
            else:
                res = max(res, me[u])
                u = p[u]
        return res
    ans = float('inf')
    me1 = set()
    for w, u, v in e1:
        me1.add((min(u,v), max(u,v)))
    for w, u, v in e:
        if (min(u,v), max(u,v)) not in me1:
            mx = get_max(u, v)
            if w > mx:
                cc = c1 + (w - mx)
                ans = min(ans, cc)
            elif w < mx:
                cc = c1 - (mx - w)
                ans = min(ans, cc)
    if ans == float('inf') or ans == c1:
        print(-1)
    else:
        print(ans)