dist = lambda xa,ya,xb,yb: abs(xa-xb) + abs(ya-yb)
get = lambda: map(int, input().split())
dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]
def bfs(x, y, c):
    queue = [(x,y)]
    visited = set()
    dist = 0
    while queue:
        dlen = len(queue)
        while dlen > 0:
            x,y = queue.pop(0)
            if (x,y) not in visited:
                visited.add((x,y))
                for d in range(1,5):
                    nx,ny = x+dx[d],y+dy[d]
                    if (nx,ny) not in visited and 0<nx<=10 and 0<ny<=10:
                        queue.append((nx,ny))
            dlen -= 1
        dist += 1
        if dist > c:
            return visited
    return visited

T = int(input())
for test in range(T):
    M, A = get()
    xA,yA,xB,yB = 1,1,10,10

    moveA = [0, *list(get())]
    moveB = [0, *list(get())]
    aps, ap_dict = {},{}
    charged = 0

    for ap in range(A):
        x, y, c, p = get()
        coverage = bfs(x, y, c)
        for x,y in coverage:
            ap_dict[ap] = p
            if (x,y) in aps:
                aps[(x,y)].append(ap)
            else:
                aps[(x,y)] = [ap]

    ap_dict[-1]=0;ap_dict[-2]=0
    apA, apB = -1, -2
    for mA, mB in zip(moveA, moveB):
        xA,yA = xA+dx[mA],yA+dy[mA]
        xB,yB = xB+dx[mB],yB+dy[mB]

        if (xA,yA) in aps:
            apA = aps[(xA,yA)]
        else: apA = [-1]
        if (xB,yB) in aps:
            apB = aps[(xB,yB)]
        else: apB = [-2]

        max_charge = 0
        for i in apA:
            for j in apB:
                if i != j: charge = ap_dict[i] + ap_dict[j]
                else: charge = ap_dict[i]
                max_charge = max(max_charge, charge)
        charged += max_charge
    print(f"#{test+1} {charged}")
