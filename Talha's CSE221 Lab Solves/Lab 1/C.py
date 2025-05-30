a = input().split()
x, y = int(a[0]), int(a[1])
b = input()
c = list(map(int, b.split(' ')))
d = c[:y]
for i in range(1, len(d)+1):
    print(d[-i], end = ' ')