#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        map = {}
        for idx in range(len(s)):
            char = s[idx]
            other_char = t[idx]

            if char not in map and other_char not in map:
                map[other_char] = char
                map[char] = other_char
                
            else:
                if char in map and map[char] != other_char: return False
                if other_char in map and map[other_char] != char: return False
                

                
            
        return True

# @lc code=end

sol = Solution()

s = "badc"
t = "baba"

print(sol.isIsomorphic(s, t))
