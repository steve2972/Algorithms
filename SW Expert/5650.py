import sys
sys.stdin = open("input.txt", "r")

T=int(input())
dr = [0,-1,0,1]
dc = [-1,0,1,0]

def turn(d,wall):
    assert 0<wall<=5
    if wall==1: dirs = [1,3,0,2]
    elif wall==2: dirs = [3,2,0,1]
    elif wall==3: dirs = [2,0,3,1]
    elif wall==4: dirs = [2,3,1,0]
    else: dirs = [2,3,0,1]
    return dirs[d]
    
def play(r,c,d):
    old_r,old_c = r,c
    bounced = 0
    while True:
        tile = grid[r][c]
        if 0<tile<=5: 
            d = turn(d,tile)
            bounced += 1
        elif tile>5:
            idx = wormholes[tile].index((r,c))
            r,c = wormholes[tile][1-idx]

        nr,nc = r+dr[d],c+dc[d]
        if 0<=nr<N and 0<=nc<N: r,c = r+dr[d],c+dc[d]
        else:
            d = (d+2)%4
            bounced+=1
        if (r,c) == (old_r,old_c) or grid[r][c]==-1: break
    return bounced


for t in range(1,T+1):
    N=int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    wormholes = {}
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 5:
                if grid[r][c] not in wormholes:
                    wormholes[grid[r][c]] = [(r,c)]
                else:
                    wormholes[grid[r][c]].append((r,c))
    
    max_score=0
    for r in range(N):
        for c in range(N):
            if grid[r][c]==0:
                for d in range(4):
                    max_score = max(max_score, play(r,c,d))
    print(f"#{t}",max_score)