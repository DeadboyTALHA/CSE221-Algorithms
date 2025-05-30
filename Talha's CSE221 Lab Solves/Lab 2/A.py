N, S = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = N - 1
flag = False
while l < r:
    if arr[l] + arr[r] == S:
        print(l + 1, r + 1)
        flag = True
        break
    elif arr[l] + arr[r] < S:
         l += 1
    else:
         r -= 1
if flag == False:
     print(-1)