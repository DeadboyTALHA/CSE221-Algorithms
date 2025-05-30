a, b = map(int, input().split())
ans = 1
a = a % 107
while b > 0:
    if b % 2 == 1:
        ans = (ans * a) % 107
    a = (a * a) % 107
    b = b // 2
print(ans)