def find_plus(r, c, grid):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    max_len = 10**9
    for dr, dc in dirs:
        cnt = 1
        while True:
            nr, nc = r + dr * cnt, c + dc * cnt
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 'G':
                cnt += 1
            else: break
        max_len = min(max_len, cnt-1)

    all_visited = []
    for i in range(max_len+1):
        visited = set()
        for j in range(i+1):
            for dr, dc in dirs:
                nr, nc = r + dr * j, c + dc * j
                visited.add((nr, nc))
        all_visited.append(visited)
    return all_visited

def twoPluses(grid):
    results = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'G':
                results.extend(find_plus(r, c, grid))

    results.sort(key=lambda x: len(x), reverse=True)

    max_size = 0
    for i in range(len(results)):
        for j in range(i+1, len(results)):
            if not results[i] & results[j]:
                max_size = max(max_size, len(results[i]) * len(results[j]))

    return max_size


if __name__ == '__main__':
    import sys

    sys.stdin = open('input.txt', 'r')

    grid = []

    for _ in range(12):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(result)