def solution(n, computers):
    paths = []
    for i in range(n):
        path = {i}
        for j in range(n):
            if j != i and computers[i][j]:
                path.add(j)
        paths.append(path)

    def search(visited, idx):
        if idx not in visited:
            visited.add(idx)
            can_go = paths[idx]
            for path in can_go:
                search(visited, path)

    all_visited = set()
    for idx in range(n):
        visited = set()
        search(visited, idx)
        if str(visited) not in all_visited:
            all_visited.add(str(visited))

    return len(all_visited)


n = 3
computers = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
]

computers2 = [
    [1, 1, 0, 0], 
    [1, 1, 1, 0], 
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]

computers3 = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

print(solution(3, computers2))