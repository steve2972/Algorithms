R,C,k = map(int, input().split())
R,C = R-1,C-1
grid = [list(map(int, input().split())) for _ in range(3)]

def row(grid):
    max_len, ans = 0, []
    for r in range(len(grid)):
        tmp, row = [0]*101, []
        for c in range(len(grid[0])):
            tmp[grid[r][c]] += 1

        tmp2 = [[] for _ in range(101)]
        for i in range(1, 101):
            if tmp[i] > 0: tmp2[tmp[i]].append(i)
        for i in range(1, 101):
            if len(tmp2[i]) > 0: 
                for j in tmp2[i]: row.extend([j, i])

        max_len = max(max_len, len(row[:100]))
        ans.append(row[:100])
    for r in ans: r.extend([0]*(max_len-len(r)))
    return ans

def transpose(grid):
    ans = []
    for c in range(len(grid[0])):
        tmp = []
        for r in range(len(grid)):tmp.append(grid[r][c])
        ans.append(tmp)
    return ans

def solve(grid):
    for i in range(101):
        if R<len(grid) and C<len(grid[0]):
            if grid[R][C] == k: return i
        if len(grid) >= len(grid[0]): grid = row(grid)
        else: grid = transpose(grid); grid = row(grid); grid = transpose(grid)
    return -1

print(solve(grid))