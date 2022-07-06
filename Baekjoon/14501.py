n = int(input())
t, p = [], []
for _ in range(n): 
    i, j = map(int, input().split())
    t.append(i)
    p.append(j)

def solve(t, p, idx):
    total = 0
    for i in range(idx, n):
        if i+t[i] <= n: 
            recursive_sum = p[i] + solve(t, p, i+t[i])
            total = max(total, recursive_sum)
    return total
print(solve(t, p, 0))
