n = int(input())
x, y = map(int, input().split())
move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
ans = []
for i, j in move:
    x1, y1 = x + i, y + j
    if 1 <= x1 <= n and 1 <= y1 <= n:
        ans += [(x1, y1)]
ans.sort()
print(len(ans))
for i in ans:
    print(i[0], i[1])