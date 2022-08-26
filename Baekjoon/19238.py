from queue import PriorityQueue as pq

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dest(r,c,tr,tc):
    p = pq()
    p.put((0,r,c))
    cost = {}
    cost[(r,c)]=0
    while not p.empty():
        _, r,c = p.get()
        if (r,c)==(tr,tc): return cost[(r,c)]
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]!=1:
                ncost = cost[(r,c)] + 1
                if (nr,nc) not in cost or ncost < cost[(nr,nc)]:
                    cost[(nr,nc)] = ncost
                    p.put((ncost+abs(tr-nr)+abs(tc-nc),nr,nc))
    return -1

n,m,k=map(int,input().split())
minus = lambda x: int(x)-1
grid = [[*map(int,input().split())] for _ in range(n)]
tr,tc = map(minus,input().split())
mdict = {}

for i in range(m):
    r,c,nr,nc=map(minus,input().split())
    s = dest(r,c,nr,nc)
    if s<0: print(-1); exit()
    mdict[i] = (r,c,s,nr,nc)
    
for _ in range(m):
    lens,mlen = [],1e9
    for p in mdict.keys():
        r,c,_,_,_=mdict[p]
        if abs(r-tr)+abs(c-tc)<=mlen:
            tmp = dest(tr,tc,r,c)
            if 0<=tmp<=mlen:
                mlen=tmp
                lens.append((tmp,r,c,p))
    if not lens: print(-1);exit()
    s,r,c,p = min(lens)
    k-=s
    if k < 0: print(-1);exit()
    s,tr,tc = mdict[p][2:]
    if k < s: print(-1);exit()
    k += s
    del mdict[p]
print(k)