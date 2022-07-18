n = int(input())
curves = []
for _ in range(n): curves.append(list(map(int, input().split())))

grid = [[0 for _ in range(101)] for _ in range(101)]
ds = [(0,1),(-1,0),(0,-1),(1,0)]

def dragon(x, y, d, g):
    tmp = [(y,x)]
    dirs = [d]
    nr, nc = y+ds[d][0], x+ds[d][1]
    tmp.append((nr,nc))
    count = 0
    while g > 0 and count < g:
        nds = []
        for d in dirs[::-1]:
            nd = (d+1)%4
            dr, dc = ds[nd]
            r, c = tmp[-1]
            tmp.append((r+dr, c+dc))
            nds.append(nd)
        dirs.extend(nds)
        count += 1
    return tmp

for x, y, d, g in curves:
    for r, c in dragon(x, y, d, g):
        if 0<=r<101 and 0<=c<101: grid[r][c] = 1

squares = 0
for r in range(100):
    for c in range(100):
        square = ([r,c],[r+1,c],[r,c+1],[r+1,c+1])
        if sum([grid[y][x] for y, x in square]) == 4: squares += 1
print(squares)