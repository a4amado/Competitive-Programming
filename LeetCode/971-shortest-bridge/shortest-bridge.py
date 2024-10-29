from typing import List, Deque
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        n = len(grid)
        q: Deque[tuple[int, int]] = deque([])
        visited = set()

        def dfs(row: int, col: int):
            if not(0 <= row < n and 0 <= col < n): return
            if (row, col) in visited or grid[row][col] != 1: return
            
            visited.add((row, col))
            q.append((row, col))
            
            for dy, dx in directions:
                dfs(row + dy, col + dx)

        # Find first island using DFS
        found_first = False
        for r in range(n):
            if found_first: break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found_first = True
                    break

        # BFS to find shortest path to second island
        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dy, dx in directions:
                    new_row, new_col = row + dy, col + dx
                    
                    if not (0 <= new_row < n and 0 <= new_col < n):
                        continue
                    
                    if (new_row, new_col) in visited:
                        continue
                        
                    # Found the second island
                    if grid[new_row][new_col] == 1:
                        return distance
                        
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))
            
            distance += 1
            
        return distance

