n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
pgrid = [[[] for _ in range(n)]for _ in range(n)]
pawns = []
for i in range(k): 
    r,c,d = map(lambda x: int(x)-1, input().split())
    pawns.append([r,c,d])
    pgrid[r][c].append(i)
dx = [1,-1,0,0]
dy = [0,0,-1,1]
turn = lambda d: d+1 if d % 2 == 0 else d-1
check = lambda r,c: 0<=r<n and 0<=c<n and grid[r][c] != 2
def move(idx, r,c,d):
    nr,nc = r+dy[d],c+dx[d]
    cur = pgrid[r][c]
    pawn_idx = cur.index(idx)+1
    cur = cur[:pawn_idx]
    if grid[nr][nc] == 1: cur = cur[::-1]
    for i in cur: pawns[i][0] = nr; pawns[i][1] = nc
    pgrid[r][c] = pgrid[r][c][pawn_idx:]
    pgrid[nr][nc] = [*cur, *pgrid[nr][nc]]

def solve():
    for m in range(1000):
        for idx, (r,c,d) in enumerate(pawns):
            nr,nc = r+dy[d],c+dx[d]
            if check(nr,nc): move(idx,r,c,d)
            else:
                nd = turn(d)
                nr,nc = r+dy[nd],c+dx[nd]
                pawns[idx][2] = nd
                if check(nr,nc): move(idx,r,c,nd)
            if len(pgrid[r][c]) >= 4: return m+1
            elif check(nr,nc):
                if len(pgrid[nr][nc]) >= 4: return m+1
    return -1
print(solve())