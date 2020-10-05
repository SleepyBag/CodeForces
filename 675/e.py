s = input()
cs = ['']
ans = []
poped = False
for c in s[::-1]:
    if not poped and c == cs[-1] and c > cs[-2]:
        cs.pop()
        poped = True
    else:
        poped = False
        cs.append(c)
    if len(cs) <= 11:
        ans.append((len(cs) - 1, ''.join(cs[::-1])))
    else:
        ans.append((len(cs) - 1, (''.join(cs[:3]) + '...' + ''.join(cs[-5:]))[::-1]))

for a, b in ans[::-1]:
    print(a, b)
