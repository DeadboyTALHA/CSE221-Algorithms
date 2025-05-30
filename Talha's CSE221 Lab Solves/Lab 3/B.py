def pairs(arr):
    s = []
    for i in arr:
        s += [i ** 2]
    m = -float('inf')
    n = arr[0]
    for j in range(1, len(arr)):
        sum = n + s[j]
        if sum > m:
            m = sum
        if arr[j] > n:
            n = arr[j]
    return m
N = int(input())
a = list(map(int, input().split()))
print(pairs(a))