blue = [[0]*6 for _ in range(4)]
green = [[0]*6 for _ in range(4)]

def find(t,x):
    for i in range(6):
        if t[x][i]==1: return i-1
    return 5

def place(t,x,y):
    b = find(blue,x)
    g = find(green,y)
    if t==1: blue[x][b]=1; green[y][g]=1
    elif t==2:
        blue[x][b]=1; blue[x][b-1]=1
        g = min(g,find(green,y+1))
        green[y][g]=1; green[y+1][g]=1     
    elif t==3:
        b = min(b,find(blue,x+1))
        blue[x][b]=1; blue[x+1][b]=1
        green[y][g]=1; green[y][g-1]=1
check = lambda t,c: sum([t[r][c] for r in range(4)])
shift = lambda t,r,c: [0,*t[r][:c],*t[r][c+1:]]
change = lambda t,c: [shift(t,r,c) for r in range(4)]

score = 0
n = int(input())
for _ in range(n):
    t,x,y=map(int,input().split())
    place(t,x,y)
    flag=0
    for c in range(2, 6):
        if check(blue,c)==4:
            score += 1
            blue=change(blue,c)
        if check(green,c)==4:
            score += 1
            green=change(green,c)
    for c in range(2):
        if check(blue,c): blue=change(blue,5)
        if check(green,c): green=change(green,5)
ans=0
for r in range(4):
    for c in range(6):
        ans+=blue[r][c]
        ans+=green[r][c]
print(score)
print(ans)
