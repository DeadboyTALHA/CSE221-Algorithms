n = int(input())
for i in range(n):
    a = input().split(' ')
    m = int(a[1])
    n = int(a[3])
    if a[2] == '+':
        print(float(m + n))
    if a[2] == '-':
        print(float(m - n))
    if a[2] == '*':
        print(float(m * n))
    if a[2] == '/':
        print(float(m / n))