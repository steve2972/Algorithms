from copy import deepcopy
grid = [[0]*4 for _ in range(4)]
fish = {}
info = [list(map(int,input().split())) for _ in range(4)]
for r in range(4):
    for c in range(4):
        n,d=info[r][c*2],info[r][c*2+1]-1
        fish[n]=r,c,d
        grid[r][c]=n

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
turn = lambda d: (d+1)%8
check = lambda r,c: 0<=r<4 and 0<=c<4
check2 = lambda r,c,nr,nc,d: check(r+dy[d],c+dx[d]) and (r+dy[d],c+dx[d])!=(nr,nc)

def move_fish(fish, grid, num,sr,sc):
    if num not in fish: return
    r,c,d=fish[num]
    for _ in range(7):
        nr,nc = r+dy[d],c+dx[d]
        if check2(r,c,sr,sc,d):
            if grid[nr][nc]:
                new_fish = grid[nr][nc]
                nd = fish[new_fish][2]
                if new_fish: fish[num],fish[new_fish] = (nr,nc,d),(r,c,nd)
                else: fish[num] = nr,nc,d
            else: fish[num] = (nr,nc,d)
            grid[r][c],grid[nr][nc]=grid[nr][nc],grid[r][c]
            return
        else: d=turn(d)

ans = 0
def dfs(fish, grid, size,sr,sc):
    global ans
    nf,ng = deepcopy(fish),[r[:] for r in grid]
    f = ng[sr][sc]
    sd = nf[f][2]
    size+=f
    del nf[f]; ng[sr][sc]=0
    for i in range(1,17): move_fish(nf, ng, i,sr,sc)
    moves = [(sr+i*dy[sd],sc+i*dx[sd]) for i in range(1,4) if check(sr+i*dy[sd],sc+i*dx[sd]) and ng[sr+i*dy[sd]][sc+i*dx[sd]]>0]
    if len(moves)==0:
        ans=max(ans,size)
        return
    for nr,nc in moves:
        dfs(nf,ng,size,nr,nc)
dfs(fish,grid,0,0,0)
print(ans)