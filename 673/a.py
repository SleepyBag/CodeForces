from math import ceil, floor

t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for ai in a[1:]:
        if ai < k:
            ans += floor((k - ai) / a[0])
    print(ans)
