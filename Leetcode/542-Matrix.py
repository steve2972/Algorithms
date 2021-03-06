from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]: mat[i][j] = -1
                else: queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0<=i+x<len(mat) and 0<=j+y<len(mat[0]) and mat[i+x][j+y] == -1:
                    mat[i+x][j+y] = mat[i][j] + 1
                    queue.append((i+x, j+y))
        return mat

