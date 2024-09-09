#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        def expand_arndound_the_center(l: int, r: int):

            if l < 0 or r >= len(s):
                return ""
            if not s[l] == s[r]:
                return ""

            terminate = False

            while l >= 0 and l < len(s)  and not terminate:
                new_r = r + 1
                new_l = l - 1

                if new_l >= 0 and new_r < len(s) and s[new_l] == s[new_r]:
                    l = new_l
                    r = new_r
                else:
                    terminate = True

            return s[l:r+1]

        curr = ""
        for i in range(len(s) - 1):
            if len(curr) == len(s):
                return s
            odd = expand_arndound_the_center(i , i)
            even = expand_arndound_the_center(i , i + 1)
            
            curr = max([curr, odd, even], key=len)
        return curr
        
# @lc code=end

s= Solution()
print(s.longestPalindrome("babad"))
