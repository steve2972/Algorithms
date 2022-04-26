from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS Solution
        visited = set()

        def BFS(i, j):
            area = 0
            queue = [(i, j)]
            while queue:
                i, j = queue.pop(0)
                if (i, j) not in visited:
                    visited.add((i,j))
                    area += 1
                    for x, y in [(1,0),(0,1),(-1,0),(0,-1)]:
                        if 0<= i+x < len(grid) and 0<=j+y < len(grid[0]) and grid[i+x][j+y]:
                            queue.append((i+x, j+y))
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(BFS(i, j), max_area)
                    
        return max_area

    def maxAreaOfIsland2(self, grid):
        # DFS Solution
        m, n = len(grid), len(grid[0])

        # Recursively turn 1 into 0
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1)
            return 0

        areas = [dfs(i,j) for i in range(m) for j in range(n)]
        return max(areas) if areas else 0

solution = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid2 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

print(solution.maxAreaOfIsland(grid))