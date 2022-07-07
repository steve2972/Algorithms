n, m = map(int, input().split())
r, c, d = map(int, input().split())
directions = [[-1,0],[0,1],[1,0],[0,-1]]
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))

rotate = lambda d: (d+3)%4
back = lambda d: (d+2)%4
q = [(r,c)]
clean = 0

while q:
    # 1. Clean the current position
    r, c = q.pop(0)
    if grid[r][c] == 0:
        grid[r][c] = -1
        clean += 1

    # 2. Turn left
    count = 0
    while True:
        d = rotate(d)
        nr, nc = r+directions[d][0],c+directions[d][1]
        if not grid[nr][nc]: 
            q.append((nr, nc))
            break
        else: count +=1
        if count == 4:
            bd = back(d)
            br, bc = r+directions[bd][0],c+directions[bd][1]
            if grid[br][bc] != 1: q.append((br, bc))
            break

print(clean)