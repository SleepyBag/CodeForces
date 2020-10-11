t = int(input())
for tt in range(t):
    n, k = map(int, input().split())
    s = input()
    pre = False
    cur = 0
    mid = []
    for i, c in enumerate(s):
        if c == 'W':
            if pre:
                if cur:
                    mid.append(cur)
            else:
                begin = cur
            pre = True
            cur = 0
        else:
            cur += 1
    end = cur
    # print(mid, begin, end)
    if end == n:
        ans = k * 2 - 1 if k else 0
    else:
        mid.sort()
        ans = 0
        for m in mid:
            if not k:
                break
            if k < m:
                ans += 2 * k
                k = 0
            else:
                ans += 2 * m + 1
                k -= m
        # print('remain k:', k)
        end = min(end, k)
        ans += end * 2
        k -= end
        begin = min(begin, k)
        ans += begin * 2
        k -= begin
        pre = False
        # print('added: ', ans)
        for i, c in enumerate(s):
            if c == 'W':
                ans += 2 if pre else 1
                pre = True
            else:
                pre = False
    print(ans)
