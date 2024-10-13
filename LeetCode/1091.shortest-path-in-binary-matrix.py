#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] != 0:return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == 1:return -1
            return 1
        nextCell = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        q = deque([])
        q.append((0, 0))
        level = 1
        while q:
            l = deque([])
            while q:
                row, col = q.popleft()
                if grid[row][col]  != 0: continue
                if row == len(grid) - 1 and col == len(grid[0]) - 1 : 
                    return level

                grid[row][col] = 1
                for y, x in nextCell:
                    nextRow = y  + row
                    nextCol = x  + col
                    if not (0 <= nextRow < len(grid)) or not (0 <= nextCol < len(grid[0])) or grid[nextRow][nextCol] != 0:
                        continue
                    if nextRow == len(grid) - 1 and nextCol == len(grid[0]) - 1 : return level + 1
                    
                    
                    l.append((nextRow, nextCol))
            q = l
            level += 1
        return -1

# @lc code=end
s = Solution()

grid = [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]
print(s.shortestPathBinaryMatrix(grid))

# grid = [[0,0,0],[1,1,0],[1,1,0]]
# print(s.shortestPathBinaryMatrix(grid))

# grid = [[1,0,0],[1,1,0],[1,1,0]]
# print(s.shortestPathBinaryMatrix(grid))

# grid = [[0]]
# print(s.shortestPathBinaryMatrix(grid))


# grid = [[0,0],[0,1]]
# print(s.shortestPathBinaryMatrix(grid))