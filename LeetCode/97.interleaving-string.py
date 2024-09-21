#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def backtracking(sf: str, idx1:int, idx2: int):
            key = (sf, idx1, idx2)


            if len(sf) > 0 and not s3.startswith(sf):
                memo[key] = False
                return memo[key]
            
            if len(sf) == len(s3) and len(s1) + len(s2) == len(s3) and sf == s3:
                memo[key] = True
                return memo[key]
            

            if key in memo:
                return memo[key]
            
            one = backtracking(sf + s1[idx1], idx1 + 1, idx2) if idx1 < len(s1) else False
            if one :
                return True
            two = backtracking(sf + s2[idx2], idx1, idx2 + 1) if idx2 < len(s2) else False
            if two :
                return True
            
            memo[key] = False
            return memo[key]
        memo = {}
        return backtracking("", 0 ,0)

# @lc code=end

s = Solution()

print(s.isInterleave("a", "b", "a"))
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
 


 