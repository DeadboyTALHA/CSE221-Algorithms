n = int(input())
a = input()
b = list(map(int, a.split(' ')))
c = input()
d = list(map(int, c.split(' ')))
count = 0
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if d[j] > d[min_idx]:
            min_idx = j
        if d[j] == d[min_idx] and b[j] < b[min_idx]:
                min_idx = j
    if min_idx != i:
        b[i], b[min_idx] = b[min_idx], b[i]
        d[i], d[min_idx] = d[min_idx], d[i]
        count += 1
print(f"Minimum swaps: {count}")
for k in range(n):
    print(f"ID: {b[k]} Mark: {d[k]}")