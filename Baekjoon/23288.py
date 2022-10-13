n,m,k=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
dice = [[4,1,3,6], [2,1,5,6]]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
d,ans = 0,0
r,c=0,0
def rotate(d,dice):
    x_d,y_d = dice
    d = [1,3,0,2][d]
    p = 1 if d%2==0 else -1
    if d<2:
        x_d = x_d[p:]+x_d[:p]
        y_d[1],y_d[-1]=x_d[1],x_d[-1]
    else:
        y_d = y_d[p:]+y_d[:p]
        x_d[1],x_d[-1]=y_d[1],y_d[-1]
    return [x_d,y_d]
def bfs(r,c,ref):
    q = [(r,c)]
    v = set()
    while q:
        r,c = q.pop(0)
        if (r,c) not in v:
            v.add((r,c))
            for d in range(4):
                nr,nc=r+dy[d],c+dx[d]
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc]==ref and (nr,nc) not in v: q.append((nr,nc))
    return len(v)
for _ in range(k):
    if not(0<=r+dy[d]<n and 0<=c+dx[d]<m): d = (d+2)%4
    dice=rotate(d,dice)
    r,c=r+dy[d],c+dx[d]
    a,b,cnt=dice[0][-1],grid[r][c],0
    if a>b: d=(d+1)%4
    elif a<b: d=(d+3)%4
    ans+=b*bfs(r,c,b)
print(ans)