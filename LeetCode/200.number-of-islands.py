#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        memo: List[List[bool]] = [[False for x in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for rowIdx, row in enumerate(grid):
            for colIdx, col in enumerate(row):
                if col == "1" and  notmemo[rowIdx][colIdx] :
                    self.dfs(grid, rowIdx, colIdx, memo)
                    count += 1
        return count
        
    def dfs(self, grid: List[List[str]], row: int, col: int, memo: List[List[bool]]):
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        
        # if out of bound
        if row < 0 or col < 0 or row > maxRow or col > maxCol:
            return False
        
        if grid[row][col] == "0":
            return False
        
        # if visited
        if memo[row][col]:
            return False
        
        memo[row][col] = True

        self.dfs(grid, row - 1, col, memo)
        self.dfs(grid, row + 1, col, memo)
        self.dfs(grid, row, col - 1, memo)
        self.dfs(grid, row, col + 1, memo)


# @lc code=end

