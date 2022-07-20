n, m, k = map(int, input().split())
grid = [list(map(lambda x: int(x), input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, t = map(int, input().split())
    trees[r-1][c-1].append(t)
ngrid = [[5]*n for _ in range(n)]
for _ in range(k):
    for r in range(n):
        for c in range(n):
            tmp, nn = [], 0
            for age in trees[r][c]:
                if age <= ngrid[r][c]: 
                    ngrid[r][c] -= age
                    tmp.append(age+1)
                else: nn += age//2    
            ngrid[r][c] += nn
            trees[r][c] = tmp
    for r in range(n):
        for c in range(n):
            ngrid[r][c] += grid[r][c]
            for age in trees[r][c]:
                if age % 5 == 0:
                    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1, 1), (-1,-1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0<=nc<n: trees[nr][nc].insert(0, 1)
ans = 0
for r in range(n):
    for c in range(n): ans += len(trees[r][c])
print(ans)