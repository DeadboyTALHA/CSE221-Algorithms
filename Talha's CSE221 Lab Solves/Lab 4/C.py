n = int(input())
a_mat = []
for i in range(n):
    r = [0] * n
    a_mat.append(r)
for i in range(n):
    s = list(map(int, input().split()))
    p = s[0]
    for j in range(1, p + 1):
        a_mat[i][s[j]] = 1
for i in a_mat:
    ans = ' '.join(map(str, i))
    print(ans)