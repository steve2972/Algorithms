n = int(input())
l = [list(map(int,input().split())) for _ in range(n**2)]
cur = {}
empty = set([(r,c) for r in range(n) for c in range(n)])
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
calc = lambda r,c,nr,nc: abs(nr-r)+abs(nc-c)
for i in l:
    s,pref = i[0], i[1:]
    t,t2 = {},{}
    for r,c in empty:
        t[(r,c)] = 0
        for p in pref:
            if p in cur:
                if calc(r,c,cur[p][0],cur[p][1])== 1: t[(r,c)] += 1
    mv = max(t.values())
    t = [i for i in t.keys() if t[i]==mv]
    if len(t)==1:
        cur[s] = t[0]
        empty.remove(t[0])
    else:
        for r,c in t: t2[(r,c)] = sum([1 for dr,dc in dirs if calc(r,c,r+dr,c+dc)==1 and (r+dr,c+dc) in empty])
        mv = max([t2[j] for j in t])
        t2 =[i for i in t2 if t2[i]==mv]
        t2.sort()
        cur[s] = t2[0]
        empty.remove(t2[0])
ans=0
for i in l:
    s,pref = i[0], i[1:]
    t=0
    for p in pref:
        if calc(cur[p][0],cur[p][1],cur[s][0],cur[s][1])==1: t+=1
    ans += 10**(t-1) if t else 0
print(ans)