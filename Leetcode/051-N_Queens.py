from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def convert_arr(arr):
            return  [''.join(['Q' if arr[i][j] == 1 else '.' for j in range(n)]) for i in range(n)]


        def update_board(arr, row, col, erase:bool=0):
            for i in range(row+1, n): 
                arr[i][col] -= 1
                offset = i - row
                if col + offset < n: arr[i][col + offset] = arr[i][col + offset] +  1 if erase else arr[i][col + offset] - 1
                if col - offset >= 0: arr[i][col-offset] = arr[i][col-offset] + 1 if erase else arr[i][col-offset] - 1


        list_arrs = list()
        stack = list()
        def DFS_queen(arr, row, col):
            # 0 not visited, -1 visited, >0 not available
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                arr[row][col] = 1
                update_board(arr, row, col)
                for i in range(n):
                    if row+1 < n and arr[row+1][i] == 0: DFS_queen(arr, row+1, i)
                if row == n-1: list_arrs.append(convert_arr(arr))
                update_board(arr, row, col, erase=1)
            return None

        for i in range(n): 
            arr = [[0]*n for i in range(n)]
            DFS_queen(arr, 0, i)
        
        return list_arrs
    
solution = Solution()
print(solution.solveNQueens(4))