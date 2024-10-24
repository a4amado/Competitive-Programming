#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for idx in range(len(haystack) - len(needle)  +1):
            sub_string = haystack[idx:idx+len(needle)]
            if needle == sub_string:return idx
        return -1

# @lc code=end

sol = Solution()
haystack = "hello"
needle = "ll"

print(sol.strStr(haystack, needle))