#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

from typing import List

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(min(strs)) == 0:
            return ""

        n = ""


        for i in range(len(min(strs))):
            curr = ''
            isAllTheSame = True
            for c in range(len(strs)):
                if c == 0:
                    curr = strs[c][i]
                else:
                    if curr != strs[c][i]:
                        return n
            n += curr
        return n
        
                        
s = Solution()
print(s.longestCommonPrefix(["a"]))
# @lc code=end

