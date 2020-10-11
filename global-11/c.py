import os
import sys
from io import BytesIO, IOBase
r, n = map(int, input().split())
ts = [0]
xs = [1]
ys = [1]
ans = [0]
maxans = [0]

def toolong(i, j):
    dis = abs(xs[i] - xs[j]) + abs(ys[i] - ys[j])
    return dis > ts[i] - ts[j]

for i in range(1, n + 1):
    t, x, y = map(int, input().split())
    ts.append(t)
    xs.append(x)
    ys.append(y)
    curans = -int(1e9)
    for j in range(i - 1, -1, -1):
        if maxans[j] < curans:
            break
        if not toolong(i, j):
            curans = max(curans, ans[j])
    curans += 1
    ans.append(curans)
    maxans.append(max(maxans[-1], curans))
# print(ans)
# print(maxans)
print(maxans[-1])
