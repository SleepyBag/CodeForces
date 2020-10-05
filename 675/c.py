mod = int(1e9 + 7)
s = input()
ans = 0
cur = 0
p = 1
m = 0
for n in s[::-1]:
    m += 1
    n = int(n)
    ans += n * cur
    ans %= mod
    # if m > 1:
    #     ans += n * p
    left = len(s) - m
    ans += (n * p) % mod * (1 + left) * left // 2
    ans %= mod
    # print(m, p, cur)
    # print(n, ans)
    cur += m * p
    cur %= mod
    p *= 10
    p %= mod
print(ans % mod)
