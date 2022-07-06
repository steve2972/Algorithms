n=int(input())
students=map(int,input().split())
b,c=map(int, input().split())
seen,total={},0
for s in students:
    if s in seen: total+=seen[s]
    else:
        ts = max((s-b),0)   # Check for negative case
        r=0 if ts==0 or ts%c==0 else 1
        add = 1 + ts//c + r
        seen[s]=add
        total+=add
print(total)