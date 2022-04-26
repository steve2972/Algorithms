from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited, queue = set(), [(sr, sc)]
        oldColor = image[sr][sc]
        while queue:
            i, j = queue.pop(0)
            visited.add((i,j))
            image[i][j] = newColor
            for x, y in [(1,0), (0, 1), (-1, 0), (0,-1)]:
                if 0<= i+x < len(image) and 0<=j+y < len(image[0]):
                    if image[i+x][j+y] == oldColor and (i+x,j+y) not in visited:
                        queue.append((i+x, j+y))
        return image

solution = Solution()
image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

print(solution.floodFill(image, sr, sc, newColor))