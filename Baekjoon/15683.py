from copy import deepcopy

n, m = map(int, input().split())
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))
cctv_list = []
for i in range(n):
    for j in range(m): 
        if grid[i][j] in range(1,6): cctv_list.append((grid[i][j], i,j))
directions = [(-1,0),(0,1),(1,0),(0,-1)]
right = lambda d: (d+1)%4
back = lambda d: (d+2)%4
left = lambda d: (d+3)%4
safe_min = 1e9

def cctv(c, d):
    if c == 1: return [directions[d]]
    elif c == 2: return [directions[d], directions[back(d)]]
    elif c == 3: return [directions[d], directions[right(d)]]
    elif c == 4: return [directions[left(d)], directions[d], directions[right(d)]]
    elif c == 5: return directions

def look(grid, ctype, r, c, d):
    dirs = cctv(ctype, d)
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        while 0<=nr<n and 0<=nc<m:
            if grid[nr][nc] == 6: break 
            grid[nr][nc] = '#'
            nr, nc = nr+dr, nc+dc
    return grid

def dfs(grid, level):
    global safe_min
    if level == len(cctv_list):
        count = 0
        for i in range(n): count += grid[i].count(0)
        safe_min = min(safe_min, count)
        return
    ctype, r, c = cctv_list[level]
    ds = [0,4,2,4,4,1][ctype]
    for d in range(ds):
        ngrid = look(deepcopy(grid), ctype, r, c, d)
        dfs(ngrid, level+1)

dfs(grid, 0)
print(safe_min)