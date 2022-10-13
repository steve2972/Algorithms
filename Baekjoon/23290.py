m,s=map(int,input().split())
h=lambda x:int(x)-1
fish = [map(h,input().split()) for _ in range(m)]
sr,sc=map(h,input().split())
grid = [[{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0} for _ in range(4)] for _ in range(4)]
for r,c,d in fish: grid[r][c][d]+=1
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]


dx = [0,-1,0,1]
dy = [-1,0,1,0]
paths = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            paths.append((i,j,k))

smells = [set(), set(), set()]
for _ in range(s):
    smells = [set(),smells[0],smells[1]]
    magic = [i[:] for i in grid]
    ngrid = [[{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0} for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in range(8):
                if grid[r][c][d]:
                    old_d,flag,cnt=d,0,grid[r][c][d]
                    nr,nc = r+dr[d],c+dc[d]
                    while (nr,nc) in smells[1] or (nr,nc) in smells[2] or (nr,nc)==(sr,sc) or not (0<=nr<4 and 0<=nc<4):
                        d = (d+7)%8
                        nr,nc = r+dr[d],c+dc[d]
                        if d==old_d: flag=1;break
                    if flag: ngrid[r][c][d]+=cnt
                    else: ngrid[nr][nc][d]+=cnt
    grid = ngrid
    scores = []
    npaths = []
    for path in paths:
        ngrid = [i[:] for i in grid]
        nsr,nsc=sr,sc
        tmp,f = 0,0
        for d in path:
            nsr,nsc=nsr+dy[d],nsc+dx[d]
            if 0<=nsr<4 and 0<=nsc<4: 
                tmp+=sum(ngrid[nsr][nsc].values())
                ngrid[nsr][nsc]={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
            else: f=1
        if not f:
            scores.append(tmp)
            npaths.append(path)
    m = max(scores)
    for i in range(len(scores)):
        if scores[i]==m: path=npaths[i];break
    
    for d in path:
        sr,sc=sr+dy[d],sc+dx[d]
        if sum(grid[sr][sc].values())>0:
            grid[sr][sc]={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0}
            smells[0].add((sr,sc))
    for i in range(4):
        for j in range(4):
            for d in range(8):
                grid[i][j][d] += magic[i][j][d]
print(sum([sum(grid[r][c].values()) for r in range(4) for c in range(4)]))