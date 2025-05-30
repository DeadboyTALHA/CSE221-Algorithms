from collections import deque
n = int(input())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
vis = []
q = deque()
q += [(x1, y1)]
c = 0
for i in range(n):
    a = []
    for j in range(n):
        a += [-1]
    vis += [a]
vis[x1][y1] = 0
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
while len(q) > 0:
    x, y = q.popleft()
    for i in moves:
        nx = x + i[0]
        ny = y + i[1]
        if (0 <= nx < n) and (0 <= ny < n):
            if vis[nx][ny] == -1:
                vis[nx][ny] = vis[x][y] + 1
                q += [(nx, ny)]
print(vis[x2][y2])