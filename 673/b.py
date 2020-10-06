t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    group = {}
    cnt = 0
    for ai in a:
        if ai == k / 2:
            cnt += 1
        else:
            group[ai] = 0
            group[k - ai] = 1
    ans = []
    cnt //= 2
    cur = 0
    for ai in a:
        if ai in group:
            ans.append(group[ai])
        elif cur < cnt:
            ans.append(0)
            cur += 1
        else:
            ans.append(1)
    print(' '.join(map(str, ans)))
