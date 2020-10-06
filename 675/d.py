import os
import sys
from io import BytesIO, IOBase

# region fastio
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------------------
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
