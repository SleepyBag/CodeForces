t = int(input())

def f(*a):
    ans = int(1e19)
    for i in a:
        ans = min(ans, sum(abs(n - i) for n in a))
    # print(a, ans)
    return ans

for tt in range(t):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    i, j = 0, n - 1
    k, l = 0, m - 1
    ans = 0
    while i <= j:
        k, l = 0, m - 1
        while k <= l:
            if i != j and k != l:
                ans += f(a[i][k], a[i][l], a[j][k], a[j][l])
            elif i == j:
                ans += f(a[i][k], a[i][l])
            elif k == l:
                ans += f(a[i][l], a[j][l])
            k += 1
            l -= 1
        i += 1
        j -= 1
    print(ans)
