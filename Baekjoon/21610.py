n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
ops = [map(int,input().split()) for _ in range(m)]

def copy(r,c):
    ans=0
    for i in range(1,8,2):
        nr,nc=r+dy[i],c+dx[i]
        if 0<=nr<n and 0<=nc<n: 
            if grid[nr][nc]:ans+=1
    return ans
move = lambda r,c,s,d: ((r+s*dy[d])%n,(c+s*dx[d])%n)

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

for d,s in ops:
    clouds = [move(r,c,s,d-1) for r,c in clouds]
    for r,c in clouds: grid[r][c]+=1
    for r,c in clouds: grid[r][c]+=copy(r,c)
    old_clouds = set(clouds)
    new_clouds = [(r,c) for r in range(n) for c in range(n) if grid[r][c]>1 and (r,c) not in old_clouds]
    clouds = new_clouds
    for r,c in clouds: grid[r][c]-=2
print(sum([sum(i) for i in grid]))