#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str1 = s
        str2 = "".join(list(s)[::-1])
        dp = [
            [
                0 for _ in range(len(s) + 1)
            ] for _ in range(len(s) + 1)
        ]

        currMax = float('-inf')
        for idx in range(1, len(dp)):
            for jdx in range(1, len(dp[0])):
                if str1[idx-1] == str2[jdx-1]:
                    dp[idx][jdx] = dp[idx-1][jdx-1] + 1
                else:
                    dp[idx][jdx] = max(dp[idx-1][jdx], dp[idx][jdx -1])
                currMax = max(currMax, dp[idx][jdx])
        return currMax
        
# @lc code=end


s = Solution()
print(
    s.longestPalindromeSubseq("bbbab")
)