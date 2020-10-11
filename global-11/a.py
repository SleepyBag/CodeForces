t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = [i for i in a if i > 0]
    neg = [i for i in a if i < 0]
    zero = [i for i in a if i == 0]
    spos = sum(pos)
    sneg = -sum(neg)
    if spos == sneg:
        print("NO")
        continue
    if spos < sneg:
        pos, neg = neg, pos
    print("YES")
    ans = map(str, pos + neg + zero)
    print(' '.join(ans))
