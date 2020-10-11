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
    print(t, x, y)
    ts.append(t)
    xs.append(x)
    ys.append(y)
    curans = 0
    for j in range(i - 1, max(i - 2 * r - 1, -1), -1):
        if not toolong(i, j):
            curans = max(curans, ans[j] + 1)
    print(curans)
    if i - 2 * r - 1 >= 0:
        curans = max(curans, maxans[i - 2 * r - 1] + 1)
    print(curans)
    ans.append(curans)
    maxans.append(max(maxans[-1] if maxans else 0, curans))
print(ans)
print(maxans)
print(maxans[-1])
