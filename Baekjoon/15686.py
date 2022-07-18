n, m = map(int, input().split())
grid, chicken, houses = [], [], []
for r in range(n):
    tmp = []
    for c, t in enumerate(list(map(int, input().split()))):
        tmp.append(t)
        if t == 1: houses.append((r,c))
        elif t == 2: chicken.append((r,c))
    grid.append(tmp)


def comb(arr, n):
    if n == 0: return [[]]
    ans = []
    for i in range(len(arr)):
        x, r = arr[i], arr[i+1:]
        for r in comb(r, n-1): ans.append([x, *r])
    return ans

min_val = 1e9
for cmb in comb(chicken, m):
    tmp = 0
    for h in houses: tmp += min(map(lambda c: abs(h[0] - c[0]) + abs(h[1]-c[1]), cmb))
    min_val = min(min_val, tmp)
print(min_val)