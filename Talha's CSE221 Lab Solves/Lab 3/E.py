def createBST(arr, l, r):
    if l > r:
        return []
    mid = (l + r) // 2
    root = arr[mid]
    left = createBST(arr, l, mid - 1)
    right = createBST(arr, mid + 1, r)
    return [root] + left + right

N = int(input()) - 1
A = list(map(int, input().split()))
ans = createBST(A, 0, N)
print(' '.join(map(str, ans)))