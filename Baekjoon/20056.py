n,m,k = map(int,input().split())
grid = [[[] for _ in range(n)] for _ in range(n)]
balls=[] 

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

def move(r,c,nb):
    m,s,d=grid[r][c].pop(0)
    r,c = (r+s*dy[d])%n,(c+s*dx[d])%n
    grid[r][c].append((m,s,d))
    nb.add((r,c))

for _ in range(m):
    r,c,m,s,d = map(int,input().split())
    balls.append((r-1,c-1))
    grid[r-1][c-1].append((m,s,d))


for _ in range(k):
    nb = set() 
    for r,c in balls: move(r,c,nb)
    balls=[]
    for r,c in nb:
        rc = grid[r][c]
        if len(rc)>1:
            m,s,d,f=0,0,rc[0][2]%2,0
            for nm,ns,nd in rc:
                m+=nm;s+=ns
                if nd%2!=d: f=1
            nm,ns = m//5,s//len(rc)
            if nm > 0:
                ds = range(1,8,2) if f else range(0,7,2)
                grid[r][c] = [(nm,ns,i) for i in ds]
                balls.extend([(r,c) for _ in range(4)])
            else: grid[r][c] = []
        else: balls.append((r,c))

ans=0
for r,c in balls:
    m,s,d=grid[r][c].pop()
    ans+=m
print(ans)