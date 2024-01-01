#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
from curses.ascii import isalnum, isalpha


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        low = 0
        high = len(s) - 1




        while low <= high:
            # if both alphabrtical
            # compare
            if ( isalnum(s[low])) and (isalnum(s[high])):
                if s[low].lower() != s[high].lower():
                    return False
                else:
                    low += 1
                    high -= 1
            elif not isalnum(s[low]):
                low += 1
            else:
                high -= 1
        return True
# s = Solution()
# s.isPalindrome("A man, a plan, a canal: Panama")
# @lc code=end

