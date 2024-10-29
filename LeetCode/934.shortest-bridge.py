# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
from typing import List, Deque, Dict
from collections import deque

# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directons = [(1,0),(-1,0),(0,1), (0,-1)]
        q: Deque[tuple[int, int]] = deque([])
        visited = set()

        def dfs(row: int, col: int, q: Deque[tuple[int, int]]):
            if not(0 <= row < len(grid) and 0 <= col < len(grid[0])):return
            if (row, col) in visited:return
            if grid[row][col] != 1: return
            q.append((row, col))
            visited.add((row, col))
            for dy, dx in directons:
                dfs(row + dy, col + dx, q)

        # Find first island
        found = False
        for rdx, row in enumerate(grid):
            if found: break
            for cdx, col in enumerate(row):
                if col == 1:
                    dfs(rdx, cdx, q)
                    found = True
                    break

        # BFS to second island
        level = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dy, dx in directons:
                    new_row = row + dy
                    new_col = col + dx
                    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])): continue
                    if (new_row, new_col) in visited: continue
                    
                    # Found second island
                    if grid[new_row][new_col] == 1:
                        return level
                        
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))
            level += 1
        
        return -1

# @lc code=end

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
sol = Solution()
print(sol.shortestBridge(grid))

grid = [
        [0,1,0],
        [0,0,0],
        [0,0,1]
    ]
print(sol.shortestBridge(grid))

grid = [[0,1,0],[0,0,0],[0,0,1]]
print(sol.shortestBridge(grid))