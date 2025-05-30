n, m = map(int, input().split())
a_mat = []
for i in range(n):
    r = [0] * n
    a_mat.append(r)
for i in range(m):
    u, v, w = map(int, input().split())
    a_mat[u - 1][v - 1] = w
for i in a_mat:
    ans = ' '.join(map(str, i))
    print(ans)