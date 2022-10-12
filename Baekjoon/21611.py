# Lessons learned:
# - always check the range of indexes found
# - always check for all zero cases
# - carefully read the instructions
# - lambda and filter are your friends
n,m=map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
ops = [map(int,input().split()) for _ in range(m)]
dr= [0,1,0,-1]
dc= [-1,0,1,0]
def g2q():
    r=c=n//2
    cnt,d,q,l_idx,idx=1,0,[],[0,[],[],[],[]],-1
    while True:
        for _ in range(2):
            for _ in range(cnt):
                r+=dr[d];c+=dc[d];idx+=1
                if r<0 or c<0: return q, l_idx
                if c==n//2:
                    if r<n//2: l_idx[1].append(idx)
                    else: l_idx[2].append(idx)
                elif r==n//2:
                    if c<n//2: l_idx[3].append(idx)
                    else: l_idx[4].append(idx)
                q.append(grid[r][c])
            d=(d+1)%4
        cnt+=1
def pop(q):
    ref,cnt,total,ans,nq = q[0],0,0,0,q[:]
    for idx,i in enumerate([*q,0]):
        if i==ref: cnt+=1
        else:
            if cnt >3:
                nq[idx-cnt-total:] = q[idx:]
                ans += ref*cnt
                total+=cnt
            ref,cnt=i,1
    return nq,ans
ans=0
q,l_idx = g2q()
for d,s in ops:
    for i in l_idx[d][:s]:
        if i<len(q):q[i]=0
    q=list(filter(lambda x:x>0,q))
    while True:
        if not q: print(ans);exit()
        q,a = pop(q)
        if a==0: break
        ans+=a
    ref,cnt,nq=q[0],0,[]
    for i in [*q,0]:
        if i==ref: cnt+=1
        else: 
            nq.extend([cnt,ref])
            if len(nq)>n*n: break
            ref=i;cnt=1
    q=nq[:n*n-1]
print(ans)