#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

from typing import *

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        level = 0

        q = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    q.append((row, col))
        visited = set(q.copy())
        direction = [
            (1,0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]
        while q:
            new_level = []
            while q:
                row, col = q.pop()


                for dy, dx in direction:
                    new_row = dy + row
                    new_col = dx + col
                    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])): continue
                    if (new_row, new_col) in visited: continue
                    visited.add((new_row, new_col))

                    new_level.append((new_row, new_col))
            q = new_level
            if new_level:
                level += 1
        return level if level else -1