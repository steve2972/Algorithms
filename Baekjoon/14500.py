n, m = map(int, input().split())
grid = []
for i in range(n): grid.append(list(map(int, input().split())))

directions = [[0,1], [0,-1], [1, 0], [-1,0]]

def get_square_shape(grid, r, c):
    ans = grid[r][c]
    for dr, dc in [[1,0], [0,1],[1,1]]:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m:
            ans += grid[nr][nc]
        else: return 0
    return ans

def get_shape(grid, r, c):
    check = lambda x, y: (0<=x<n) and (0<=y<m)
    ans = 0
    for dr, dc in directions:
        tmp = grid[r][c]
        if check(r+dr, c+dc):
            nr, nc = r+dr, c+dc
            tmp += grid[nr][nc]
            # Get S shape
            if dr and 0<=nr+dr<n:
                for _, p in directions[:2]:
                    if 0<= nc+p < m: ans = max(ans, sum([tmp, grid[nr][nc+p], grid[nr+dr][nc+p]]))
            elif dc and 0<=nc+dc<m:
                for p, _ in directions[2:]:
                    if 0<= nr+p < n: ans = max(ans, sum([tmp, grid[nr+p][nc], grid[nr+p][nc+dc]]))
        if check(r+2*dr, c+2*dc):
            nr, nc = r+2*dr, c+2*dc
            tmp += grid[nr][nc]
            # Get T shape and L shape
            if dr:
                for _, p in directions[:2]:
                    if 0<=c+p<m: 
                        ans = max(ans, tmp + grid[min(nr,r)+1][c+p])
                        ans = max(ans, tmp + grid[nr][c+p])
            else:
                for p, _ in directions[2:]:
                    if 0<=r+p<n: 
                        ans = max(ans, tmp + grid[r+p][min(nc,c)+1])
                        ans = max(ans, tmp+grid[r+p][nc])
        if check(r+3*dr, c+3*dc):
            # Get I shape
            ans = max(ans, tmp+grid[r+3*dr][c+3*dc])
    return ans

def get_max(grid, r, c):
    ans = max([
        get_square_shape(grid, r, c), 
        get_shape(grid, r, c)
    ])
    return ans

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, get_max(grid, i, j))
print(ans)