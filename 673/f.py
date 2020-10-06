n, m, q = map(int, input().split())
p = list(map(int, input().split()))
edge = []
query = []
for i in range(m):
    edge.append(list(map(int, input().split())))
for i in range(q):
    query.append(list(map(int, input().split())))
for qi, i in q:
