
from typing import *
from collections import deque

from typing import List
from collections import deque

class Solution:
    def nearest(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # Initialize queue with all 1s and set others to inf
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0  # Distance to itself is 0
                else:
                    grid[i][j] = float('inf')
        
        # BFS
        while q:
            row, col = q.popleft()
            for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_row, new_col = row + dy, col + dx
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] == 0: continue
                    if grid[new_row][new_col] != float('inf'):continue
                    new_dist = grid[row][col] + 1
                    grid[new_row][new_col] = new_dist
                    q.append((new_row, new_col))
        
        return grid
    


s = Solution()
print(s.nearest([[0,1,1,0],[1,1,0,0],[0,0,1,1]]))
# print(s.nearest([[1,1,1,1,1,1,0,1,0,0],
# [0,1,0,0,1,1,1,1,0,0],
# [1,0,1,0,0,0,0,1,1,0]]))
