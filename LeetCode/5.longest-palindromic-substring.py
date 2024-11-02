#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s1 = s
        s2 = s[::-1]

        length = len(s) + 1

        dp = [[0 for _ in range(length) ] for _ in range(length)]

        maxVal = 0
        position = (0, 0)
        for i in range(1, length):
            for j in range(1, length):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > maxVal:
                        maxVal = dp[i][j]
                        position = (i -1, j-1)
        return s[position[0] - maxVal + 1 : position[0] + 1]

        
        
# @lc code=end

s= Solution()
print(s.longestPalindrome("babad"))
