#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List,  Set

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(start: int, end: int):
            if start >= len(s) or end >= len(s):
                return False
            
            l, r = start, end
            
            while l < r:
                if s[l] != s[r]:return False
                l += 1
                r -= 1
            return True

        curr = []
        res = []
        def backtracking(start:int):
            if start >= len(s):
                res.append(curr.copy())
                return
            
            # handle all substrings from start to len(s) - 1
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    curr.append(s[start:i+1])
                    backtracking(i + 1)
                    curr.pop()


        backtracking(0)
        
        return res
            

# @lc code=end
s = Solution()
print(s.partition("aab"))
