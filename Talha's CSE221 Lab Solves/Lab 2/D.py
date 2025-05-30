T = int(input())
for i in range(T):
    s = input()
    l = 0
    r = len(s) - 1
    c = -1
    while l <= r:
        mid = (l + r) // 2
        if s[mid] == '1':
            c = mid + 1
            r = mid - 1
        else:
            l = mid + 1
    print(c)