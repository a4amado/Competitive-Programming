#
# @lc app=leetcode id=1219 lang=python3
#
# [1219] Path with Maximum Gold
#
from typing import *
from itertools import product
# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        direction = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(row: int, col: int):
            if not (0 <= row < rows and 0 <= col < cols): return 0
            if (row, col) in visited: return 0
            if grid[row][col] == 0:return 0
            visited.add((row, col))
            maxFromHere = float('-inf')
            val = grid[row][col]
            
            for dx, dy in direction:
                maxFromHere = max(maxFromHere , dfs(row + dy, col + dx) + val)
            visited.remove((row, col))

            return maxFromHere

        maxi = float('-inf')
        visited = set()
        for row, col in product(range(len(grid)), range(len(grid[0]))):
            if grid[row][col] != 0:
                visited.clear()
                maxi = max(maxi, dfs(row, col))
        return maxi if maxi != float('-inf') else 0