N, K = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
sum = 0
max_size = 0
for i in range(N):
    sum += arr[i]
    while K < sum:
        sum -= arr[l]
        l += 1
    if max_size < (i - l + 1):
        max_size = i - l + 1
print(max_size)
