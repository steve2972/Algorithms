import numpy as np
from itertools import permutations

def find_neighbors(board, r, c):
    neighbors = set()
    neighbors.add((r, c))
    for x, y in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        if 0 <= r+x < 4 and 0 <= c+y < 4:
            neighbors.add((r+x, c+y))
    for idx, tmp_board in enumerate([board[r, c+1:], board[r, :c], board[r+1:, c], board[:r, c]]):
        first_idx = np.argwhere(tmp_board)
        if len(tmp_board) > 0 and np.sum(tmp_board) > 0 and len(first_idx) > 0:
            first_idx = first_idx.squeeze(axis=-1)
            if idx == 0:
                neighbors.add((r, c + first_idx[0] + 1))
            elif idx == 1:
                neighbors.add((r, first_idx[-1]))
            elif idx == 2:
                neighbors.add((r + first_idx[0] + 1, c))
            else:
                neighbors.add((first_idx[-1], c))
        else:
            if idx == 0:
                neighbors.add((r, 3))
            elif idx == 1:
                neighbors.add((r, 0))
            elif idx == 2:
                neighbors.add((3, c))
            else: neighbors.add((0, c))

    neighbors.remove((r, c))
    return neighbors

def bfs(grid, i, j, target):
    moves, flag = 0, 2
    queue = [(i, j)]
    while queue:
        level_size = len(queue)
        while level_size > 0:
            i, j = queue.pop(0)
            if grid[i, j] == target: 
                grid[i, j], queue, level_size = 0, [], 0
                moves += 1
                flag -= 1
                if not flag: return i, j, moves
            for (x, y) in find_neighbors(grid, i, j):
                queue.append((x, y))
            level_size -= 1
        moves += 1

def solution(board, r, c):
    board = np.array(board, dtype=np.uint8)
    perms = list(permutations(np.arange(1, np.max(board)+1)))
    min_moves = 1e9
    for permutation in perms:
        tmp_board = np.copy(board)
        i, j = r, c
        moves = 0
        move_list = []
        for target in permutation:
            i, j, m = bfs(tmp_board, i, j, target)
            move_list.append((m, (i, j)))
            moves += m
        if moves < min_moves: min_moves = moves
    
    return min_moves


board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]

print(solution(np.array(board), 0, 1))
# print(find_neighbors(np.array(board), 1, 0))