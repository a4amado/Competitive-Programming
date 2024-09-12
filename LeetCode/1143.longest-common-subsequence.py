#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols +1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]  + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col  - 1])

        return dp[rows][cols]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]  # Corrected dimensions

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1  # Corrected recurrence
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        
        return dp[rows][cols]
# @lc code=end

s = Solution()
s.longestCommonSubsequence("abcde", "ace")