n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
for r in range(n):
    for c in range(n): 
        if grid[r][c] == 9: 
            shark = (r,c)
            grid[r][c] = 0
def find(r, c, size):
    visited, fish = set(), []
    elps = 0
    q = [(r,c)]
    while q:
        qsize = len(q)
        while qsize > 0:
            r, c = q.pop(0)
            if (r,c) not in visited:
                visited.add((r,c))
                if 0 < grid[r][c] < size: fish.append((r,c))
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] <= size:
                        q.append((nr,nc))
            qsize -= 1
        elps += 1
        if len(fish) > 0: break
    return fish, elps-1

size, full, elps = 2, 0, 0
while True:
    fish, dis = find(shark[0], shark[1], size)
    if len(fish) == 0: break
    else:
        target = fish[0]
        for f in fish[1:]:
            if f[0] < target[0]: target = f
            elif f[0] == target[0]:
                if f[1] < target[1]: target = f
        elps += dis
        shark = target
        grid[shark[0]][shark[1]] = 0
        full += 1
        if full == size:
            size += 1
            full = 0
print(elps)
