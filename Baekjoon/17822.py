n,m,t=map(int,input().split())
circles = [list(map(int,input().split())) for _ in range(n)]
ops = [list(map(int,input().split())) for _ in range(t)]

left = lambda d, k: d[k:]+d[:k]
right = lambda d, k: d[-k:]+d[:-k]
rotate = [right,left]

def close(r,c):
    l = [(r,(c+1)%m), (r,(c+m-1)%m)]
    if r == 0: l.append((r+1,c))
    elif r == n-1: l.append((r-1,c))
    else: l.extend([(r-1,c),(r+1,c)])
    return [(nr,nc) for nr,nc in l if circles[r][c]==circles[nr][nc]]

for x,d,k in ops:
    xlist,flag=list(map(lambda x:x-1,range(x,n+1,x))),0
    for i in xlist: circles[i] = rotate[d](circles[i], k)
    new = [i[:] for i in circles]
    for r in range(n):
        for c in range(m):
            tmp = new[r][c]
            if tmp>0: 
                clist = close(r,c)
                if len(clist): flag=1
                for nr,nc in clist:
                    if circles[nr][nc]==tmp: new[nr][nc]=0;new[r][c]=0
    circles=new
    if not flag:
        total,cnt=0,0
        for circle in circles: 
            tmp = list(filter(lambda x:x>0,circle))
            total += sum(tmp); cnt += len(tmp)
        if cnt>0:
            avg = total/cnt
            for r in range(n):
                for c in range(m):
                    if circles[r][c] > 0:
                        if circles[r][c] > avg: circles[r][c]-=1
                        elif circles[r][c] < avg: circles[r][c]+=1
ans = 0
for circle in circles: ans+=sum(filter(lambda x:x>0,circle))
print(ans)