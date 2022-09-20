n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
r=c=n//2
dx=[-1,0,1,0]
dy=[0,1,0,-1]
ds=[[[1,0],[-1,0]],[[1,1],[-1,1]],[[2,1],[-2,1]],[[1,2],[-1,2]],[[0,3]],[[0,2]]]
d,out=0,0
def move(r,c,d):
    global out
    nr,nc=r+dy[d],c+dx[d]
    dust = grid[nr][nc]
    grid[nr][nc]=0
    pdust = list(map(lambda x: int(x*dust), [0.01,0.07,0.02,0.1,0.05]))
    dust -= sum([2 * i for i in pdust[:-1]], pdust[-1])
    pdust.append(dust)
    for i in range(6):
        for dr, dc in ds[i]:
            if d==0: dc*=-1
            elif d==1: dr,dc=dc,dr
            elif d==3: dr,dc=-dc,dr
            if 0<=r+dr<n and 0<=c+dc<n: grid[r+dr][c+dc]+=pdust[i]
            else: out+=pdust[i]
    return nr,nc 
for m in range(1,n+1):
    if m==n:
        for m in range(n-1): r,c=move(r,c,d)
    else:
        for _ in range(2):
            for _  in range(m): r,c=move(r,c,d)
            d=(d+1)%4
print(out)
