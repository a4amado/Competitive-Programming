
from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        
        # Initialize dp table
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = dp[1][0] = 0
        
        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
        
        return dp[m][n]