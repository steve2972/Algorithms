from copy import deepcopy

def Move(marble, grid, m_type:str, marble_type:str):
    finished = 0
    n_grid = deepcopy(grid)
    if m_type == 'left':
        for c in range(marble[1]-1,-1,-1):
            if grid[marble[0]][c] == 'O': finished = 1
            elif grid[marble[0]][c] != '.': 
                next_position=(marble[0], c+1)
                break
    elif m_type == 'right':
        for c in range(marble[1]+1,len(grid[0])):
            if grid[marble[0]][c] == 'O': finished = 1
            elif grid[marble[0]][c] != '.': 
                next_position=(marble[0], c-1)
                break
    elif m_type == 'up':
        for r in range(marble[0]-1,-1,-1):
            if grid[r][marble[1]] == 'O': finished = 1
            elif grid[r][marble[1]] != '.':
                next_position=(r+1, marble[1])
                break
    elif m_type == 'down':
        for r in range(marble[0]+1,len(grid)):
            if grid[r][marble[1]] == 'O': finished = 1
            elif grid[r][marble[1]] != '.':
                next_position=(r-1, marble[1])
                break
    if finished: next_position = (0,0)
    n_grid[marble[0]][marble[1]] = '.'
    n_grid[next_position[0]][next_position[1]] = marble_type
    return next_position, finished, n_grid

def move_board(red, blue, grid, m_type:str):
    leftmost = lambda red, blue: True if red[1] < blue[1] else False
    topmost = lambda red, blue: True if red[0] < blue[0] else False

    red_first = (leftmost(red, blue) and m_type=='left') \
        or (not leftmost(red, blue) and m_type=='right') \
        or (topmost(red, blue) and m_type=='up') \
        or (not topmost(red, blue) and m_type=='down')

    if red_first:
        r, r_finished, n_grid = Move(red, grid, m_type, 'R')
        b, b_finished, n_grid = Move(blue, n_grid, m_type, 'B')
    else:
        b, b_finished, n_grid = Move(blue, grid, m_type, 'B')
        r, r_finished, n_grid = Move(red, n_grid, m_type, 'R')

    return r, r_finished, b, b_finished, n_grid

def find_marbles(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'R': red = (r, c)
            elif grid[r][c] == 'B': blue = (r, c)
    return red, blue

row, col = map(int, input().split())
grid = []
for r in range(row):
    grid.append([c for c in input()])

num_moves = 11
visited = set() # states that red marble has visited
level_tracker = {}
r, b = find_marbles(grid)

def dfs(red, blue, grid, visited, level):
    global num_moves
    if level > 10: return
    visited.add((red, blue))
    level_tracker[red] = level
    for move in ['up', 'down', 'left', 'right']:
        r, r_finished, b, b_finished, n_grid = move_board(red, blue, grid, move)
        if r_finished and not b_finished: 
            num_moves = min(level+1, num_moves)
            return
        elif (r, b) not in visited and not b_finished:
            dfs(r, b, n_grid, deepcopy(visited), level+1)
            

dfs(r, b, grid, visited, 0)
if num_moves <= 10: print(num_moves)
else: print(-1)