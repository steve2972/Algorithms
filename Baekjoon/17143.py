R,C,M = map(int, input().split())
grid = [[[] for _ in range(C)] for _ in range(R)]
sharks = {}

for i in range(M):
    r,c,s,d,z = map(int, input().split())
    sharks[z] = [r-1,c-1,s,d-1]
    grid[r-1][c-1].append(z)

dirs = [(-1,0),(1,0),(0,1),(0,-1)]

def move_shark(z):
    r,c,s,d = sharks[z]
    grid[r][c].remove(z)
    nr,nc = r+s*dirs[d][0],c+s*dirs[d][1]
    if 0<=nr<R and 0<+nc<C:
        sharks[z][0] = nr
        sharks[z][1] = nc
        grid[nr][nc].append(z)
        return
    
    if d>=2:
        if d == 2: ns = s - (C-1-c)
        else: ns = s-c
        rem = ns % (C-1)
        move = ns // (C-1)
        if (d==3 and move%2==0) or (d==2 and move%2==1):
            if rem == 0: nr, nc = r, 0; d=3 if d==2 else 2
            else: nr,nc = r, rem; d=2 if d ==3 else 2
        else:
            if rem == 0: nr,nc = r,C-1; d=2 if d ==3 else 3
            else: nr,nc = r, C-1-rem; d=3 if d==2 else 3

    else:
        if d == 1: ns = s - (R-1-r)
        else: ns = s-r
        rem = ns % (R-1)
        move = ns // (R-1)
        if (d==0 and move%2==0) or (d==1 and move%2==1):
            if rem == 0: nr, nc = 0, c; d=0 if d==1 else 1
            else: nr,nc = rem, c; d=1 if d==0 else 1
        else:
            if rem == 0: nr,nc = R-1,c; d=1 if d==0 else 0
            else: nr,nc = R-1-rem,c; d=0 if d==1 else 0
    
    sharks[z] = [nr,nc,s,d]
    grid[nr][nc].append(z)

def catch(c):
    for r in range(R):
        if grid[r][c]:
            ans = grid[r][c].pop()
            del sharks[ans]
            return ans
    return 0

total = 0
for fisher in range(C):
    total += catch(fisher)
    shark_list = list(sharks.keys())
    for shark in shark_list:
        move_shark(shark)
    for z in shark_list:
        if z in sharks:
            r, c = sharks[z][:2]
            if len(grid[r][c]) > 1:
                big = max(grid[r][c])
                for nz in grid[r][c]:
                    if nz != big and nz in sharks:
                        del sharks[nz]
                grid[r][c] = [big]
            assert len(grid[r][c]) == 1
print(total)