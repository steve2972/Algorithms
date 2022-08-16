n,m,k = map(int,input().split())
grid=[[*map(int,input().split())] for _ in range(n)]
sharks = {}
for r in range(n):
    for c in range(n):
        s = grid[r][c]
        if s:
            sharks[s] = [r,c]
            grid[r][c]=[s,k]
        else: grid[r][c] = []

dx=[0,0,-1,1]
dy=[-1,1,0,0]

minus = lambda x: int(x)-1
sd = [*map(minus,input().split())]
for s in range(1,m+1):
    sharks[s].extend([sd[s-1],[[*map(minus,input().split())] for _ in range(4)]])

check = lambda r,c: 0<=r<n and 0<=c<n
avail = lambda r,c,m,s: [d for d in m if check(r+dy[d],c+dx[d]) and (not grid[r+dy[d]][c+dx[d]] or (grid[r+dy[d]][c+dx[d]][1]==k+1))]
navail= lambda r,c,m,s: [d for d in m if check(r+dy[d],c+dx[d]) and grid[r+dy[d]][c+dx[d]][0]==s]

for i in range(1000):
    tgrid = [r[:] for r in grid]
    for s in range(m+1):
        if s in sharks:
            r,c,d,p = sharks[s]
            moves = avail(r,c,p[d],s)
            if not moves: moves = navail(r,c,p[d],s)
            if moves:
                d = moves[0]
                r,c = r+dy[d],c+dx[d]    
                if tgrid[r][c]:
                    ns = tgrid[r][c][0]
                    if s < ns: del sharks[ns]
                    elif s > ns: del sharks[s]; s=ns; _,_,d,p = sharks[s]
            tgrid[r][c] = [s,k+1]
            sharks[s] = [r,c,d,p]
    grid = tgrid
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                s,t = grid[r][c]
                if t-1 == 0: grid[r][c] = []
                else: grid[r][c] = [s,t-1]
    
    if len(sharks)==1:
        print(i+1)
        exit()
print(-1)