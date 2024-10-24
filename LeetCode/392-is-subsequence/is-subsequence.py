#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

from collections import Counter

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        found = 0
        idx = 0
        for i in s:
            is_found = False
            while idx < len(t):
                
                if t[idx] == i:
                    found += 1
                    is_found = True
                    idx += 1
                    break
                idx += 1
            if not is_found: return False
        return found == len(s)