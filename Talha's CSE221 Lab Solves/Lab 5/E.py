import sys
sys.setrecursionlimit(300000)
n, m = map(int, input().split())
g = []
for i in range(n + 1):
    g += [[]]
for i in range(m):
    u, v = map(int, input().split())
    g[u] += [v]
vis = [0] * (n + 1)
flag = [False]
stack = []
for i in range(1, n + 1):
    if vis[i] == 0:
        stack += [(i, 0)]
        temp = []
        while stack:
            a, b = stack.pop()
            if b == 1:
                vis[a] = 2
                temp.pop()
                continue
            if vis[a] == 1:
                flag[0] = True
                break
            if vis[a] == 2:
                continue
            vis[a] = 1
            stack += [(a, 1)]
            temp += [a]
            for i in g[a]:
                if vis[i] == 1:
                    flag[0] = True
                    break
                if vis[i] == 0:
                    stack += [(i, 0)]
            if flag[0] == True:
                break
    if flag[0] == True:
        break
if flag[0] == True:
    print("YES")
else:
    print("NO")