# 2048 Easy
from copy import deepcopy

n = int(input())
grid = []
for i in range(n): grid.append(list(map(int, input().split())))
# 0, 1, 2, 3 = right, left, down, up
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move_once(grid, flag, r: int, c:int, d:int):
    nr, nc = r+dy[d], c+dx[d]
    while 0<=nr<n and 0<=nc<n:
        pr, pc = nr-dy[d], nc-dx[d]
        # Check if move possible
        if grid[nr][nc] != 0:
            if grid[nr][nc] == grid[pr][pc] and not flag[nr*n + nc]:
                grid[nr][nc] <<= 1
                grid[pr][pc] = 0
                flag[nr*n + nc] = True
            break
        grid[nr][nc] = grid[pr][pc]
        grid[pr][pc] = 0
        nr, nc = nr+dy[d], nc+dx[d]

def move(grid, d):
    nrange = range(0, n)
    ngrid = deepcopy(grid)
    flag = [False for _ in range(n*n)]
    if d < 2:
        for c in nrange[::-1*dx[d]]:
            for r in nrange:
                if grid[r][c]: move_once(ngrid, flag, r, c, d)
    else:
        for r in nrange[::-1*dy[d]]:
            for c in nrange:
                if grid[r][c]: move_once(ngrid, flag, r, c, d)
    return ngrid

def get_max(grid):
    max_num = 0
    for i in grid:
        for j in i:
            max_num = max(max_num, j)
    return max_num

max_sum = 0
def dfs(grid, num_moves):
    global max_sum
    if num_moves == 5:
        max_sum = max(max_sum, get_max(grid))
        return
    for d in range(4):
        ngrid = move(grid, d)
        dfs(ngrid, num_moves+1)
        

dfs(grid, 0)
print(max_sum)