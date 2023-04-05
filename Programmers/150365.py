def solution(n, m, x, y, r, c, k):
    l1 = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
    if l1(x, y, r, c) > k: return 'impossible'
    elif (k - l1(x, y, r, c)) % 2 == 1: return 'impossible'

    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    ds = ['d', 'l', 'r', 'u']

    q = [(x, y, '', 0)]
    while q:
        x, y, s, d = q.pop(0)
        if (x,y) == (r,c) and (k - d) % 2 == 1: return "impossible"
        if (x,y) == (r,c) and d==k: return s
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if l1(nx, ny, r, c) > k - d - 1: continue
            if not (0 < nx <= n and 0 < ny <= m): continue
            q.append((nx, ny, s + ds[i], d + 1)) # type: ignore
            break
    return 'impossible'
    


print(solution(3, 4, 2, 3, 3, 1, 5))