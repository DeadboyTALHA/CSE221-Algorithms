n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    x, y = map(int, input().split())
    l = 0
    r = n
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    a = l
    l = 0
    r = n
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= y:
            l = mid + 1
        else:
            r = mid
    print(l - a)
