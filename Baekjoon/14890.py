n, l = map(int, input().split())
grid = []
for _ in range(n): grid.append(list(map(int, input().split())))

directions = [(1,0), (0,1)] # Down, Right

def check_point(r, c, d, built):
    cur_height = grid[r][c]
    dr, dc = directions[d]
    target_height = grid[r+l*dr][c+l*dc]
    if target_height == cur_height+1:
        for i in range(l):
            if grid[r+i*dr][c+i*dc] != cur_height or built[r+i*dr][c+i*dc]: return False, ()
            built[r+i*dr][c+i*dc] = True
    elif target_height == cur_height-1:
        if grid[r+dr][c+dc] == cur_height: return True, (r+dr,c+dc)
        for i in range(1, l):
            if grid[r+i*dr][c+i*dc] != cur_height-1: return False, ()
            built[r+i*dr][c+i*dc] = True
        built[r+l*dr][c+l*dc] = True
    elif grid[r+dr][c+dc] == cur_height: return True, (r+dr,c+dc)
    else: return False, ()
    return True, (r+l*dr,c+l*dc)
    

count = 0
built = [[False for _ in range(n)] for _ in range(n)]
for r in range(n):
    path, c = True, 0
    while c < n-l:
        is_path, safe = check_point(r, c, 1, built)
        if not is_path:
            path = False
            break
        _, c = safe
    for i in range(n-c):
        if grid[r][c+i] != grid[r][c]: path =  False
    if path: count += 1
built = [[False for _ in range(n)] for _ in range(n)]
for c in range(n):
    path, r = True, 0
    while r < n-l:
        is_path, safe = check_point(r, c, 0, built)
        if not is_path:
            path = False
            break
        r, _ = safe
    for i in range(n-r):
        if grid[r+i][c] != grid[r][c]: path =  False
    if path: count += 1
print(count)