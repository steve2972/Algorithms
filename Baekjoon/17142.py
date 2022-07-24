n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
avail, air= [], 0
for r in range(n):
    for c in range(n):
        if grid[r][c] == 0: air += 1
        elif grid[r][c] == 2: avail.append((r,c))
def comb(arr, n):
    if n == 0: return [[]]
    ans = []
    for i in range(len(arr)):
        x, r = arr[i], arr[i+1:]
        for r in comb(r, n-1): ans.append([x, *r])
    return ans
def spread(grid, virus, cur_min):
    q = virus
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 2 and (r,c) not in virus: grid[r][c] = -1
    t = 0
    spread = 0
    visited = set()
    if air == 0: return 0
    while q:
        qlen = len(q)
        while qlen > 0:
            r, c = q.pop(0)
            if (r,c) not in visited:
                if grid[r][c] == 0: spread += 1
                grid[r][c] = 2
                visited.add((r,c))
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc]!=1: q.append((nr,nc))
            qlen -= 1
        if spread==air or t >= cur_min: return t
        t += 1
    return -1
def print_grid(grid):
    print("#"*30)
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()
ans = 1e9
for virus in comb(avail, m):
    ngrid = [i[:] for i in grid]
    t = spread(ngrid, virus, ans)
    if t >= 0: ans = min(ans,t)
print(-1 if ans==1e9 else ans)