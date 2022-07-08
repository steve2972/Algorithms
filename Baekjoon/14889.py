n = int(input())
grid = []
for i in range(n): grid.append(list(map(int, input().split())))

def combination(arr, n):
    if n == 0: return [[]]
    ans = []
    for i in range(len(arr)):
        a, r = arr[i], arr[i+1:]
        for r in combination(r, n-1): ans.append([a, *r])
    return ans

def find_sum(arr):
    total = 0
    for idx, i in enumerate(arr):
        for j in arr[idx:]:
            total += grid[i][j]
            total += grid[j][i]
    return total

min_diff = 1e9
combs = combination(range(n), n/2)
p1, p2 = 0, len(combs)-1
while p1 <= p2:
    start, link = combs[p1], combs[p2]
    min_diff = min(min_diff, abs(find_sum(start) - find_sum(link)))
    p1 += 1
    p2 -= 1
print(min_diff)