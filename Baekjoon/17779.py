n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
def divide(x,y,d1,d2):
    mid, cnt = set(), [0]*5
    for i in range(d1):
        r,c = x+i,y-i
        for j in range(2*min(i, min(d1,d2))+1):
            if 0<=r<n and 0<=c+j<n: mid.add((r,c+j)); cnt[4] += grid[r][c+j]
    for i in range(d2+1)[::-1]:
        r,c = x+d1+i,y-d1+i
        for j in range(2*min(d2-i, min(d1,d2))+1): 
            if 0<=r<n and 0<=c+j<n: mid.add((r,c+j)); cnt[4] += grid[r][c+j]
    for r in range(x+d1):
        for c in range(y+1): 
            if (r,c) not in mid: cnt[0]+=grid[r][c]
    for r in range(x+d2+1):
        for c in range(y+1,n): 
            if (r,c) not in mid: cnt[1]+=grid[r][c]
    for r in range(x+d1,n):
        for c in range(y-d1+d2): 
            if (r,c) not in mid: cnt[2]+=grid[r][c]
    for r in range(x+d2+1,n):
        for c in range(y-d1+d2,n): 
            if (r,c) not in mid: cnt[3]+=grid[r][c]

    return max(cnt) - min(cnt)
ans = 1e9
for d1 in range(n):
    for d2 in range(n):
        for x in range(n):
            for y in range(n):
                if x+d1+d2<n and y-d1>=0 and y+d2<n:
                    ans = min(ans,divide(x,y,d1,d2))

print(ans)