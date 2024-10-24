#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
from typing import *

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (0,1),
            (0,-1),
            (-1, 0),
            (1, 0)
        ]

        def dfs(row: int, col: int):
            if not (0 <= row < len(grid) and  0<= col < len(grid[0]) ): return
            if grid[row][col] == 1: return
            grid[row][col] = 1

            for dy, dx in directions:
                dfs(row + dy, col + dx)
        
        for i in range(len(grid)):
            dfs(i, 0)
        for i in range(len(grid)):
            dfs(i, len(grid[0]) -1)

        for i in range(len(grid[0])):
            dfs(0, i)
        for i in range(len(grid[0])):
            dfs(len(grid) - 1, i)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count
            