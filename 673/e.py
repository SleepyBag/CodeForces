n = int(input())
a = list(map(int, input().split()))
cur = [a]
s = sum(a)
ans = 0
cnt = 0

i = 1 << 31
while i:
    i >>= 1
    fcnt = 0
    bcnt = 0
    nex = []
    for arr in cur:
        aa, bb = [], []
        zcnt = 0
        ocnt = 0
        for ai in arr:
            if ai & i:
                ocnt += 1
                fcnt += zcnt
                aa.append(ai)
            else:
                zcnt += 1
                bcnt += ocnt
                bb.append(ai)
        if aa:
            nex.append(aa)
        if bb:
            nex.append(bb)
    if bcnt > fcnt:
        ans |= i
        cnt += fcnt
    else:
        cnt += bcnt
    cur = nex

print(cnt, ans)
