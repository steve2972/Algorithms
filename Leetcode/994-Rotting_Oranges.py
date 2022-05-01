from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        elapsed, fresh = 0, 0
        rotten = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: fresh += 1
                elif grid[i][j] == 2: rotten.append((i, j))
        
        while rotten and fresh > 0:
            elapsed += 1
            for _ in range(len(rotten)):
                i, j = rotten.pop(0)
                for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2 # Fresh is now rotten
                        fresh -= 1
                        rotten.append((i+x, j+y))

        return elapsed if not fresh else -1


solution = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(solution.orangesRotting(grid))