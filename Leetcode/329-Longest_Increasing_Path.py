from typing import List

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if len(matrix) == 0: return 0
    m, n = len(matrix), len(matrix[0])
    cache = [[0 for i in range(n)] for j in range(m)]

    def dfs(i, j):
        if cache[i][j] != 0: return cache[i][j]
        ans = 1
        for x, y in ((i-1, j), (i, j+1), (i+1, j), (i, j-1)):
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                ans = max(ans, 1 + dfs(x, y))

        cache[i][j] = ans
        return ans

    ans = 1
    for i in range(m):
        for j in range(n):
            ans = max(ans, dfs(i, j))

    return ans



matrix = [
    [0,1,2,3,4,5,6,7,8,9],
    [19,18,17,16,15,14,13,12,11,10],
    [20,21,22,23,24,25,26,27,28,29],
    [39,38,37,36,35,34,33,32,31,30],
    [40,41,42,43,44,45,46,47,48,49],
    [59,58,57,56,55,54,53,52,51,50],
    [60,61,62,63,64,65,66,67,68,69],
    [79,78,77,76,75,74,73,72,71,70],
    [80,81,82,83,84,85,86,87,88,89],
    [99,98,97,96,95,94,93,92,91,90],
    [100,101,102,103,104,105,106,107,108,109],
    [119,118,117,116,115,114,113,112,111,110],
    [120,121,122,123,124,125,126,127,128,129],
    [139,138,137,136,135,134,133,132,131,130],
    [0,0,0,0,0,0,0,0,0,0]
]

#matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))