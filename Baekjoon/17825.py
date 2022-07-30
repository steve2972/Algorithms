dice = [*map(int,input().split())]
grid = list(range(0,41,2))
mid = [25,30,35,40]
g1=[10,13,16,19,*mid]
g2=[20,22,24,*mid]
g3=[30,28,27,26,*mid]
alt = [grid,g1,g2,g3]
def move(i, d, pn):
    pstate, n = pn[i][0], pn[i][1] + d
    if pstate==-1: return 0
    if pstate == 0:
        if n % 5 == 0 and n<20: 
            pn[i] = [n//5,0]
            return grid[n]
        elif n < 21: pn[i][1]=n; return grid[n]
    elif n < len(alt[pstate]): pn[i][1] = n; return alt[pstate][n]
    pn[i]=[-1,-1]
    return 0
total = 0
def dfs(i,ans,pawns,lvl):
    global total   
    if lvl == 10:
        total=max(total,ans)
        return
    tmp = move(i, dice[lvl], pawns)
    s = [alt[p[0]][p[1]] if p!=[-1,-1] else 0 for p in pawns]
    if pawns[i] in pawns[:i]+pawns[i+1:] and pawns[i]!=[-1,-1]: return
    elif s[i] in s[:i]+s[i+1:]:
        if s[i] in [25,35,40]: return
        elif s[i]==30 and pawns[i]!=[3,0]: 
            for p in pawns[:i]+pawns[i+1:]:
                if p!=[3,0] and alt[p[0]][p[1]]==30: return
    for j in range(4):
        if pawns[j][0]>-1: 
            dfs(j,ans+tmp,[i[:] for i in pawns],lvl+1)
dfs(0,0,[[0,0] for _ in range(4)],0)
print(total)