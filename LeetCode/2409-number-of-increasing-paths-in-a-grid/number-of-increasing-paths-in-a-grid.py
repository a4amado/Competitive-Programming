from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        R, C = len(grid), len(grid[0])
        memo = {}

        def dfs(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]
            
            paths = 1  # Current cell is always a valid path
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < R and 0 <= new_col < C and grid[new_row][new_col] > grid[row][col]:
                    paths = (paths + dfs(new_row, new_col)) % MOD
            
            memo[(row, col)] = paths
            return paths

        total_paths = 0
        for i in range(R):
            for j in range(C):
                total_paths = (total_paths + dfs(i, j)) % MOD

        return total_paths