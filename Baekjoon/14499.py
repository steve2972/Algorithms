n, m, x, y, k = map(int, input().split())
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))
actions = map(int, input().split())
actions = [i-1 for i in actions]

# 0: right, 1: left, 2: up, 3: down
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

vq = [0]*4
hq = [0]*4
shift = lambda n, d: n[d:] + n[:d]

def move_dice(d, vq, hq):
    if d < 2:
        hq = shift(hq, -dx[d])
        vq[1], vq[-1] = hq[1], hq[-1]
    else:
        vq = shift(vq, -dy[d])
        hq[1], hq[-1] = vq[1], vq[-1]
    return vq, hq

def print_dice(vq, hq):
    print(f" {vq[0]}")
    print(f"{hq[0]}{vq[1]}{hq[2]}")
    print(f" {vq[2]}")
    print(f" {vq[3]}")

def print_grid(grid):
    for i in grid:
        print(i)

moves = ['right', 'left', 'up', 'down']

r, c = x, y
for move in actions:
    nr, nc = r+dy[move],c+dx[move]
    if 0 <= nr < n and 0<= nc < m:
        vq, hq = move_dice(move, vq, hq)
        front, back = vq[1], vq[-1]
        grid_val = grid[nr][nc]
        if grid_val == 0: 
            grid[nr][nc] = back
        else: 
            vq[-1], hq[-1] = grid_val, grid_val
            grid[nr][nc] = 0
        print(front)
        r, c = nr, nc