gears, ops = [], []
for _ in range(4): gears.append(input())
n = int(input())
for _ in range(n): ops.append(list(map(int, input().split())))

rotate = lambda n, d: n[-d:] + n[:-d]
check_polarity = lambda g: [(g[i-1][2]!=g[i][-2]) for i in range(1,4)]

for op in ops:
    polarity = check_polarity(gears)
    gear, d = op
    dirs = [0]*4
    dirs[gear-1] = d
    for i in range(gear, 4):
        dirs[i] = dirs[i-1]*-1 if polarity[i-1] else 0
    for i in range(gear-2, -1, -1):
        dirs[i] = dirs[i+1]*-1 if polarity[i] else 0
    for idx, d in enumerate(dirs): gears[idx] = rotate(gears[idx], d)

print(sum([int(gears[i][0])*(2**i) for i in range(4)]))