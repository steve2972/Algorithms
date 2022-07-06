n = int(input())
k = int(input())
apples = set()
for i in range(k):
    apple_pos = input().split()
    apples.add((int(apple_pos[0]), int(apple_pos[1])))
turn_list = {}
l = int(input())
for i in range(l):
    control = input().split()
    turn_list[int(control[0])] = control[1]


def solve():
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    turn_right = lambda d: (d+1)%4
    turn_left = lambda d: (d+3)%4
    r, c = 1, 1
    d = 0
    snake = [(1, 1)]

    for t in range(1, 10001):
        dx, dy = directions[d]
        nr, nc = r+dx, c+dy
        if (nr, nc) in snake or 0 in (nr, nc) or n+1 in (nr, nc): return t
        elif (nr, nc) not in apples: snake.pop(0)
        else: apples.remove((nr, nc))
        snake.append((nr, nc))
        r, c = nr, nc
        if t in turn_list:
            if turn_list[t] == 'L': d = turn_left(d)
            elif turn_list[t] == 'D': d = turn_right(d)
    return t

print(solve())