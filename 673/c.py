t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pre = {}
    gap = {}
    for i, ai in enumerate(a):
        if ai in pre:
            gap[ai] = max(gap[ai], i - pre[ai] - 1)
        else:
            gap[ai] = i
        pre[ai] = i
    for ai in pre:
        gap[ai] = max(gap[ai], n - pre[ai] - 1)
    ans = [(gap[ai], ai) for ai in gap]
    ans.sort()
    p = 0
    cur = int(1e9)
    for i in range(n):
        while p < len(ans) and ans[p][0] <= i:
            cur = min(cur, ans[p][1])
            p += 1
        print(-1 if cur == int(1e9) else cur, end="")
        print(end=' ' if i != n - 1 else '')
    print()
