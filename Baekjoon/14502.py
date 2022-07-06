from copy import deepcopy

n, m = map(int, input().split())
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))

def virus_spread(grid, q):
    # BFS method of spreading
    check = lambda x, y: (0<=x<n) and (0<=y<m)
    while q:
        r, c = q.pop(0)
        grid[r][c] = 2
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r+dr,c+dc
            if check(nr, nc) and grid[nr][nc] == 0:
                q.append((nr,nc))

def combination(arr, n):
    if n == 0: return [[]]
    ans = []
    for i in range(len(arr)):
        x, r = arr[i], arr[i+1:]
        for r in combination(r, n-1): ans.append([x, *r])
    return ans

find = lambda grid, c: [(i,j) for i in range(n) for j in range(m) if grid[i][j] == c]
max_safe = 0
empty = find(grid, 0)
virus = find(grid, 2)
for comb in combination(empty, 3):
    ngrid = deepcopy(grid)
    for r, c in comb: ngrid[r][c] = 1
    safe = find(grid, 0)
    virus_spread(ngrid, deepcopy(virus))
    max_safe = max(max_safe, len(find(ngrid,0)))

print(max_safe)