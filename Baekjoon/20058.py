import sys
n,q = map(int,input().split())
nn = 2**n
sys.setrecursionlimit(nn**2)
grid = [list(map(int,input().split())) for _ in range(nn)]
ops = list(map(int,input().split()))
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
def rotate(r,c,l):
    for i in range(l):
        for j in range(i+1,l):
            grid[i+r][j+c], grid[j+r][i+c] = grid[j+r][i+c], grid[i+r][j+c]
    for m in range(r, r+l):
        i,j = c,c+l-1
        while i<j:
            grid[m][i], grid[m][j] = grid[m][j],grid[m][i]
            i+=1;j-=1
def melt(r,c,old):
    if not grid[r][c]: return
    f=0
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if not(0<=nr<nn and 0<=nc<nn): f+=1
        elif old[nr][nc] == 0: f+=1
        if f > 1: grid[r][c] -= 1;return

def dfs(r,c):
    if not grid[r][c]: return 0
    grid[r][c]=0
    t=1
    for dr,dc in dirs:
        nr,nc=r+dr,c+dc
        if 0<=nr<nn and 0<=nc<nn:
            if grid[nr][nc]: t += dfs(nr,nc)
    return t

for l in ops:
    nl = 2**l  
    q = [(r,c) for r in range(0, nn, nl) for c in range(0, nn, nl)]
    if l: 
        for r,c in q: rotate(r,c,nl)
    old = [i[:] for i in grid]
    for r in range(nn):
        for c in range(nn): melt(r,c,old)
print(sum([sum(i) for i in grid]))
print(max([dfs(r,c) for r in range(nn) for c in range(nn)]))