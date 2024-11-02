from itertools import groupby

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        l = groupby(s)
        max_Val = 0 
        for _, val in l:
            max_Val = max(max_Val, len(list(val)))  # Get the length of the entire group
        return max_Val
# @lc code=end

s = "leetcode"

sol = Solution()
print(sol.maxPower(s))
