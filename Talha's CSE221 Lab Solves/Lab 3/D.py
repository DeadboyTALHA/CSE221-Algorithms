def fun(a, n, m1):
    ans = 1
    while n > 0:
        if n % 2:
            ans= (ans * a) % m1
        a = (a * a) % m1
        n //= 2
    return ans
T = int(input())
for i in range(T):
    a, n, m = map(int, input().split())
    if a == 1:
        print(n % m)
    else:
        m1 = m * (a - 1)
        p = fun(a, n + 1, m1)
        ans = (p - a) // (a - 1)
        print(ans % m)