R,C,K=map(int,input().split())
heaters = []
checks = []
for r in range(R):
    for c,n in enumerate(map(int,input().split())):
        if 0<n<5: heaters.append((r,c,n-1))
        elif n==5: checks.append((r,c))
            
W = int(input())
walls = set([tuple(map(lambda x:int(x)-1,input().split())) for _ in range(W)])
grid = [[0 for _ in range(C)] for _ in range(R)]
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def check_wall(r,c,d):
    if d==0: i,j,k=r,c-1,0
    elif d==1: i,j,k=r,c,0
    elif d==2: i,j,k=r+1,c,-1
    else: i,j,k=r,c,-1
    return (i,j,k) not in walls

def heat(r,c,d,n=5):
    check = lambda r,c: (r,c) not in visited and 0<=r<R and 0<=c<C
    if not n: return
    nr,nc = r+dr[d],c+dc[d]
    avail = []
    if n==5:
        if check(nr,nc) and check_wall(nr,nc,d):
            grid[nr][nc]+=5
            heat(nr,nc,d,4)
        return
    if check_wall(nr,nc,d): avail.append((nr,nc))
    if d<2: a,b=2,3
    else: a,b=0,1
    tr1,tc1=r+dr[a],c+dc[a]
    nr1,nc1=tr1+dr[d],tc1+dc[d]
    tr2,tc2=r+dr[b],c+dc[b]
    nr2,nc2=tr2+dr[d],tc2+dc[d]
    if check_wall(tr1,tc1,a) and check_wall(nr1,nc1,d): avail.append((nr1,nc1))
    if check_wall(tr2,tc2,b) and check_wall(nr2,nc2,d): avail.append((nr2,nc2))
    
    for r,c in avail:
        if check(r,c):
            visited.add((r,c))
            grid[r][c]+=n
            heat(r,c,d,n-1)

choco=0
while True:
    for r,c,d in heaters:
        visited = set()
        heat(r,c,d)
    ngrid = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            ngrid[r][c]+=grid[r][c] 
            for d in range(4):
                nr,nc=r+dr[d],c+dc[d]
                if 0<=nr<R and 0<=nc<C and check_wall(nr,nc,d):
                    if grid[nr][nc]<grid[r][c]:
                        share = (grid[r][c]-grid[nr][nc])//4
                        ngrid[nr][nc]+=share
                        ngrid[r][c]-=share
    grid = ngrid
    for r in range(R):
        if r==0 or r==R-1: crange=range(C)
        else: crange=[0,-1]
        for c in crange:
            if grid[r][c]>0: grid[r][c]-=1
    choco+=1
    if choco>100: break

    cnt=0
    for r,c in checks:
        if grid[r][c] >= K: cnt+=1
    if cnt==len(checks): print(choco);exit()
print(101)