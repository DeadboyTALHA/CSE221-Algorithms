import heapq
n = int(input())
w = []
g = []
ind = []
us = []
flag1 = True
for i in range(n):
    s = input()
    w += [s]
for i in range(26):
    g += [[]]
    ind += [0]
    us += [False]
for i in range(n):
    for j in range(len(w[i])):
        ch = w[i][j]
        us[ord(ch) - ord('a')] = True
for i in range(n - 1):
    w1 = w[i]
    w2 = w[i + 1]
    m = min(len(w1), len(w2))
    flag2 = False
    for j in range(m):
        a = ord(w1[j]) - ord('a')
        b = ord(w2[j]) - ord('a')
        if a != b:
            flag3 = False
            for k in range(len(g[a])):
                if g[a][k] == b:
                    flag3 = True
                    break
            if flag3 == False:
                g[a] += [b]
                ind[b] += 1
            flag2 = True
            break
    if flag2 == False:
        if len(w1) > len(w2):
            flag1 = False
            break
if flag1 == False:
    print(-1)
else:
    hp = []
    ans = []
    c = 0
    for i in range(26):
        if us[i] and ind[i] == 0:
            heapq.heappush(hp, i) 
    while len(hp) > 0:
        u = heapq.heappop(hp)
        ans += [u]
        for i in range(len(g[u])):
            v = g[u][i]
            ind[v] -= 1
            if ind[v] == 0:
                heapq.heappush(hp, v)
    for i in range(26):
        if us[i]:
            c += 1
    if len(ans) != c:
        print(-1)
    else:
        res = ""
        for i in range(len(ans)):
            res += chr(ans[i] + ord('a'))
        print(res)