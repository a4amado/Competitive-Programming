#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Create a 2D DP table initialized with 0s
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right cell contains the length of the LCS
        return dp[m][n]
 
# @lc code=end

s = Solution()
s.longestCommonSubsequence("abcde", "ace")