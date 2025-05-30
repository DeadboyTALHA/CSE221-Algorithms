def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, q = map(int, input().split())
ans = [None] * (n + 1)
for i in range(1, n + 1):
    ans[i] = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and gcd(i, j) == 1:
            ans[i] += [j]
for i in range(1, n + 1):
    ans[i].sort()
for i in range(q):
    x, k = map(int, input().split())
    if k <= len(ans[x]):
        print(ans[x][k - 1])
    else:
        print(-1)