def merge(a, b):
    res = []
    i = 0
    j = 0
    c = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
            c += len(a) - i
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    return res, c

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    a1, m = mergeSort(arr[:mid])
    a2, n = mergeSort(arr[mid:])
    ans, p = merge(a1, a2)
    count = m + n + p
    return ans, count

N = int(input())
a = list(map(int, input().split()))
ans, count = mergeSort(a)
print(count)
print(' '.join(map(str, ans)))