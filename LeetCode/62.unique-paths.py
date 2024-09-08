#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for x in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]


s = Solution()
s.uniquePaths(3, 7)
# @lc code=end

