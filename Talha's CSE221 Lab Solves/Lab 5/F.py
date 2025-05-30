R, H = map(int, input().split())
g = []
count = 0
vis = []
for i in range(R):
    s = list(input())
    g += [s]
for i in range(R):
    temp = []
    for j in range(H):
        temp += [False]
    vis += [temp]
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
for r in range(R):
    for c in range(H):
        if vis[r][c] == False and g[r][c] != '#':
            q = [(r, c)]
            vis[r][c] = True
            if g[r][c] == 'D':
                count1 = 1
            else:
                count1 = 0
            z = 0
            while z < len(q):
                x1, y1 = q[z]
                z += 1
                for i in range(4):
                    x2 = x1 + x[i]
                    y2 = y1 + y[i]
                    if 0 <= x2 < R and 0 <= y2 < H:
                        if vis[x2][y2] == False and g[x2][y2] != '#':
                            vis[x2][y2] = True
                            q += [(x2, y2)]
                            if g[x2][y2] == 'D':
                                count1 += 1
            if count1 > count:
                count = count1
print(count)