N, K = map(int, input().split())
fish = list(map(int, input().split()))
hrange = []

for i in range(2,N):
    tmp = list(range(i,1,-1))
    for _ in range(2): hrange.extend(tmp)


steps = 0
while True:
    # 1. Add fish to mins
    min_fish = min(fish)
    for i in range(N):
        if fish[i] == min_fish: fish[i] += 1
    # 2. stack the fish
    grid = [[0 for _ in range(N)] for _ in range(N)]
    grid[-1] = fish
    cnt=0

    for i in range(N):
        w=N
        for j in range(i+1,N):
            if grid[-2][j]==0: w = j;break
        tmp = []
        coords = []
        for j in range(N)[::-1]:
            if grid[j][i]:
                tmp.append(grid[j][i])
                coords.append((j,i))
            else: break

        if w+len(tmp) > N: break
        for r,c in coords: grid[r][c]=0

        grid[N-hrange[i]][w:w+len(tmp)] = tmp

    # 3. Move the fish
    def move_fish(g):
        dr=[0,0,1,-1]
        dc=[1,-1,0,0]
        movement = {}
        for r in range(len(g)):
            for c in range(len(g[0])):
                if g[r][c]:
                    movement[(r,c)]=[]
                    for d in range(4):
                        nr,nc = r+dr[d],c+dc[d]
                        if 0<=nr<len(g) and 0<=nc<len(g[0]):
                            if g[nr][nc]:
                                rm = g[r][c] - g[nr][nc]
                                if rm > 0:
                                    movement[(r,c)].append((nr,nc,rm//5))
        for (r,c) in movement.keys():
            for nr,nc,d in movement[(r,c)]:
                g[r][c]-=d
                g[nr][nc]+=d
        return g
    grid = move_fish(grid)
    # 4. Change the fish
    fish = []
    for c in range(N):
        for r in range(N)[::-1]:
            if grid[r][c]: fish.append(grid[r][c])

    fish_top = fish[:len(fish)//2][::-1]
    fish_bot = fish[len(fish)//2:]

    fish = [fish_top,fish_bot]

    fish_bot = [fish[0][N//4:], fish[1][N//4:]]
    fish_top = [fish[1][:N//4][::-1], fish[0][:N//4][::-1]]
    fish = []
    for i in fish_top: fish.append(i)
    for i in fish_bot: fish.append(i)

    # 5. Move the fish again
    fish = move_fish(fish)
    nfish = []
    for c in range(len(fish[0])):
        for r in range(len(fish))[::-1]:
            nfish.append(fish[r][c])

    fish=nfish
    k = max(fish) - min(fish)
    steps += 1
    if k <= K: print(steps);exit()
