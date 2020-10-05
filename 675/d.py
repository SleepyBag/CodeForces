n, m = map(int, input().split())
sx, sy, fx, fy = map(int, input().split())

def get_dis(x, y, fx, fy):
    return abs(fx - x) + abs(fy - y)

def ins_dis(x, y, fx, fy):
    return min(abs(fx - x), abs(fy - y))

edge = [[] for i in range(m + 2)]
# ans = dis(sx, sy, fx, fy)
ps = []
for i in range(m):
    x, y = map(int, input().split())
    ps.append((i + 1, x, y))
    edge[0].append((i + 1, ins_dis(sx, sy, x, y)))
    edge[i + 1].append((m + 1, get_dis(fx, fy, x, y)))
    # print(ans, x, y)
# print(ans)
ps.sort(key=lambda a: a[1])
for i in range(len(ps)):
    if i > 0:
        edge[ps[i][0]].append((ps[i - 1][0], ps[i][1] - ps[i - 1][1]))
    if i < len(ps) - 1:
        edge[ps[i][0]].append((ps[i + 1][0], ps[i + 1][1] - ps[i][1]))

ps.sort(key=lambda a: a[2])
for i in range(len(ps)):
    if i > 0:
        edge[ps[i][0]].append((ps[i - 1][0], ps[i][2] - ps[i - 1][2]))
    if i < len(ps) - 1:
        edge[ps[i][0]].append((ps[i + 1][0], ps[i + 1][2] - ps[i][2]))

from heapq import *
q = [(0, 0)]
inf = int(1e19)
dis = [inf for i in range(m + 2)]
s = [False for i in range(m + 2)]
while q:
    curdis, cur = heappop(q)
    if not s[cur]:
        s[cur] = True
        for nex, d in edge[cur]:
            if curdis + d < dis[nex]:
                dis[nex] = curdis + d
                heappush(q, (curdis + d, nex))

# print(dis)
print(min(dis[-1], get_dis(sx, sy, fx, fy)))
