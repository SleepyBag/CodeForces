from math import floor, ceil

t = int(input())
for tt in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % n != 0:
        print(-1)
    else:
        mean = s // n
        print(3 * (n - 1))
        for i in range(1, n):
            cur = a[i] % (i + 1)
            if cur == 0:
                cur = i + 1
            print(1, i + 1, i + 1 - cur)
            print(i + 1, 1, ceil(a[i] / (i + 1)))
        for i in range(1, n):
            print(1, i + 1, mean)
