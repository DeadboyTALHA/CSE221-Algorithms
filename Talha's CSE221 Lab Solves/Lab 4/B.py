n, m = map(int, input().split())
a_list = {}
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
for i in range(1, n + 1):
    a_list[i] = []
for i in range(m):
    a_list[u[i]] += [(v[i], w[i])]
for i, j in a_list.items():
    print(f'{i}: ', end = '')
    for k in j:
        print(k, end = ' ')
    print()