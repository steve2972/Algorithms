n, m, h = map(int, input().split())
lines = []
for _ in range(m): lines.append(list(map(lambda x: int(x)-1, input().split())))
lad = [[0 for _ in range(n-1)] for _ in range(h)]

def check_avail(l):
    avail = set()
    for r in range(h):
        for c in range(n-1):
            flag = 1
            for dc in range(-1, 2):
                if 0<= c+dc < n-1:
                    if l[r][c+dc] ==1: flag = 0
            if flag: avail.add((r, c))
    return avail

def travel(lad, c):
    for r in range(h):
        if c == 0:
            if lad[r][0]: c += 1
        elif c == n-1:
            if lad[r][n-2]: c -= 1
        else:
            if lad[r][c-1]: c -= 1
            elif lad[r][c]: c += 1
    return c

check = lambda lad: [1 if travel(lad, c) != c else 0 for c in range(n-1)]
min_val = 4
visited = set()

def dfs(lad, lvl):
    global min_val
    k = check(lad)
    if not sum(k):
        min_val = min(min_val, lvl)
        return
    if sum(k) > 2 * (3-lvl): return
    if lvl == 3: return
    visited.add(str(lad))
    avail = check_avail(lad)

    for r, c in avail:
        if lvl > 1 and not k[c]:
            pass
        else:
            nl = [j[:] for j in lad]
            nl[r][c] = 1
            if str(nl) not in visited: dfs(nl, lvl+1)

for r, c in lines: lad[r][c] = 1

dfs(lad, 0)
if min_val == 4: min_val = -1
print(min_val)