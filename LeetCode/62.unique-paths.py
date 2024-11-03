#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(m)]for _ in range(n)]

        for i in range(1,n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[-1][-1]

s = Solution()
print(s.uniquePaths(3, 7))
# @lc code=end

