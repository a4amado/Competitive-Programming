#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
from typing import *
# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        
        def dfs(row:int, col: int, visited: Dict):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])): return
            if (row, col) in visited: return
            if grid[row][col] == 0: return
            visited[(row, col)] = True
            grid[row][col] = 0

            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)
        
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                dfs(0, i, {})
            if grid[-1][i] == 1:
                dfs(len(grid) - 1, i, {})

        for i in range(len(grid)):
            if grid[i][0] == 1:
                dfs(i, 0, {})
            if grid[i][-1] == 1:
                dfs(i, len(grid[0]) - 1, {})

        count = 0
        visited = {}
        for rowIdx, row in enumerate(grid):
            for colIDx, col in enumerate(row):
                if col == 1:
                    count += 1
        return count
# @lc code=end
s = Solution()
print(s.numEnclaves([[0,0,1,1,1,0,1,1,1,0,1],[1,1,1,1,0,1,0,1,1,0,0],[0,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,0,0,0,1],[0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,1,0,0,1]]))


