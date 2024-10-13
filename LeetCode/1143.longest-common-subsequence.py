#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

from typing import *

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)

        def d(idx1: int, idx2: int, memo: Dict):
            if idx1 == rows or idx2 == cols: return 0
            key = (idx1, idx2)
            if key in memo: return memo[key]
            res = 0
            if text1[idx1] == text2[idx2]:
                res = 1 + d(idx1 + 1, idx2 + 1, memo)
            else:
                res = max(d(idx1 + 1, idx2,  memo), d(idx1, idx2 + 1,  memo))
            memo[key] = res
            return memo[key]
        memo = {}

        # dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        curr = [0 for _ in range(cols + 1)]
        prev = [0 for _ in range(cols + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j], curr[j-1])
            curr, prev = prev, curr

        return prev[cols]
s = Solution()
print(
    s.longestCommonSubsequence("abcde", "ace")
)

