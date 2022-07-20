n, l, m = map(int, input().split())
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))

def bfs(visited, r, c):
    q = [(r,c)]
    total = []
    tmp = set()
    while q:
        r, c = q.pop(0)
        if (r,c) not in visited:
            visited.add((r,c))
            tmp.add((r,c))
            total.append(grid[r][c])
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n:
                    if l <= abs(grid[nr][nc] - grid[r][c]) <= m: q.append((nr,nc))
    avg = sum(total) // len(total)
    for r, c in tmp: grid[r][c] = avg
    return len(total) > 1

days = 0
while True:
    flag = False
    visited = set()
    for r in range(n):
        for c in range(n):
            if (r,c) not in visited: 
                flag = bfs(visited, r, c) or flag
    if not flag: break
    else: days += 1

print(days)