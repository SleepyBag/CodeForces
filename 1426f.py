n = int(input())
s = input()
mod = int(1e9 + 7)

ans = [1, 0, 0, 0]

for _, c in enumerate(s):
    nex = []
    # print(ans)
    if c == 'c':
        ans[3] += ans[2]
    elif c == 'b':
        ans[2] += ans[1]
    elif c == 'a':
        ans[1] += ans[0]
    else:
        ans[3] = ans[3] * 3 + ans[2]
        ans[2] = ans[2] * 3 + ans[1]
        ans[1] = ans[1] * 3 + ans[0]
        ans[0] *= 3
    for i in range(4):
        ans[i] %= mod
    # print(ans)
    # print()
print(ans[-1])
