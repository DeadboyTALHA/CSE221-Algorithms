N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
i = 0
j = 0
ans = []
while i < N and j < M:
    if a[i] <= b[j]:
        ans += [a[i]]
        i += 1
    else:
        ans += [b[j]]
        j += 1
while i < N:
    ans += [a[i]]
    i += 1
while j < M:
    ans += [b[j]]
    j += 1
print(" ".join(map(str, ans)))