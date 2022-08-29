n,k = map(int,input().split())
belt = [*map(int,input().split())]
bots = [0 for _ in range(n)]
spin = lambda arr: arr[-1:] + arr[:-1]
ans,e=0,0
while e<k:
    ans+=1
    belt=spin(belt); bots=spin(bots)
    if bots[-1]: bots[-1]=0
    for i in range(n-1)[::-1]:
        if bots[i] and belt[i+1] and not bots[i+1]:
            bots[i+1]=1; bots[i]=0
            belt[i+1]-=1
            if not belt[i+1]: e+=1
    if belt[0]: 
        bots[0]=1; belt[0]-=1
        if not belt[0]: e+=1
    if bots[-1]: bots[-1]=0
print(ans) 