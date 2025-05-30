n = int(input())
a = []
b = []
c = []
for i in range(n):
  s = input().split(' ')
  a += [s[0]]
  t1, t2 = map(int, s[-1].split(":"))
  b += [(t1 * 60) + t2]
  c += [s]

for i in range(n - 1):
  flag = False
  for j in range(n - i -1):
    if a[j] > a[j + 1]:
      a[j], a[j + 1] = a[j + 1], a[j]
      b[j], b[j + 1] = b[j + 1], b[j]
      c[j], c[j + 1] = c[j + 1], c[j]
      flag = True
    elif a[j] == a[j + 1] and b[j] < b[j + 1]:
      a[j], a[j + 1] = a[j + 1], a[j]
      b[j], b[j + 1] = b[j + 1], b[j]
      c[j], c[j + 1] = c[j + 1], c[j]
      flag = True
  if flag == False:
    break
for i in range(n):
  ans = ' '.join(c[i])
  print(ans)