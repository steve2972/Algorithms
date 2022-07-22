R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

def find_dust(grid):
    dust = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0: dust.append((r,c))
    return dust

for i in range(R): 
    if grid[i][0] == -1: cleaner = (i, i+1); break

upper = [(0,1),(-1,0),(0,-1), (1,0)]
lower = [(0,1),(1,0),(0,-1),(-1,0)]


for _ in range(T):
    # Step 1: Fine dust spread
    tmp = [[0]*C for _ in range(R)]
    for r, c in find_dust(grid):
        count = 0
        for dr, dc in upper:
            nr,nc=r+dr,c+dc
            if 0<=nr<R and 0<=nc<C and grid[nr][nc] >= 0:
                tmp[nr][nc] += grid[r][c] // 5
                count += 1
        grid[r][c] -= (grid[r][c]//5) * count
    for r in range(R):
        for c in range(C):
            if tmp[r][c] > 0: grid[r][c] += tmp[r][c]
    # Step 2: Air Cleaner
    r, c, tmp = cleaner[0],0,0
    for dr, dc in upper:
        while 0<=r+dr<=cleaner[0] and 0<=c+dc<C:
            nr,nc=r+dr,c+dc
            grid[nr][nc],tmp = tmp,grid[nr][nc]
            r,c=nr,nc
    grid[r][c] = -1

    r, c, tmp = cleaner[1],0,0
    for dr, dc in lower:
        while cleaner[1]<=r+dr<R and 0<=c+dc<C:
            nr,nc=r+dr,c+dc
            grid[nr][nc],tmp = tmp,grid[nr][nc]
            r,c=nr,nc
    grid[r][c] = -1


ans = 2
for r in grid: ans += sum(r)
print(ans)