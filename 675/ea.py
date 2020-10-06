s = input()
n = len(s)
res = ['',s[-1]]
l = [1]
flag = True
last = ['']
for i in range(n-2,-1,-1):
    tmp = res[-1]
    if flag and s[i]==tmp[0] and s[i]>last[-1]:
        res.append(res[-2])
        l.append(l[-1]-1)
        flag = False
        if l[-1]>0 and res[-1][0]!=s[i]:
            last.pop()
    else:
        l.append(l[-1]+1)
        tmp = s[i]+tmp
        flag = True
        if len(tmp)>10:
            res.append(tmp[:5]+'...'+tmp[-2:])
        else:
            res.append(tmp)
        if len(res[-1])>1 and res[-1][0]!=res[-1][1]:
            last.append(res[-1][1])
res.pop(0)
for i in range(n-1,-1,-1):
    print(l[i],res[i])
