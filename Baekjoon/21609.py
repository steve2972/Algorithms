# Remember to always check visited during BFS!

n,m=map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
def fall():
    for c in range(n):
        for r in range(n)[::-1]:
            if grid[r][c] >= 0:
                nr = r
                while nr+1<n and grid[nr+1][c] == -2: nr+=1
                if nr!=r:
                    grid[nr][c] = grid[r][c]
                    grid[r][c]=-2
def find(r,c):
    ref = grid[r][c]
    q = [(r,c)]
    rw = 0
    rl = []
    v = set()
    while q:
        r,c = q.pop(0)
        if (r,c) not in v:
            if grid[r][c]==0: rw+=1
            else: rl.append((r,c))
            v.add((r,c))
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in v:
                    if grid[nr][nc]==ref or grid[nr][nc]==0: q.append((nr,nc))
    rl.sort()
    return v, rw, rl[0]
ans = 0
while True:
    mg,av = [],set()
    for r in range(n):
        for c in range(n):
            if grid[r][c]>0 and grid[r][c]>0 and (r,c) not in av:
                v, rw, rb = find(r,c)
                for i in v: av.add(i)
                if len(v) >= 2: mg.append((len(v),rw,rb,v))
    if len(mg)==0: break
    mg.sort(reverse=True)
    ans += mg[0][0]**2
    for r,c in mg[0][-1]: grid[r][c] = -2
    fall()
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[n-1-j][i] = grid[i][j]
    grid = a
    fall()
print(ans)