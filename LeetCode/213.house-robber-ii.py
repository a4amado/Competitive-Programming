#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        curr = 0
        prev = 0

        for i in range(0, len(nums) - 1):
            new_max = prev + nums[i]
            prev = curr
            curr = max(new_max, curr)
        
        mm = max(curr, prev)

        curr = 0
        prev = 0
        for i in range(1, len(nums)):
            new_max = prev + nums[i]
            prev = curr
            curr = max(new_max, curr)
        
        m = max(curr, prev, mm)
        
        return m
        
# @lc code=end

s  = Solution()
print(s.rob([1,2,3,1]))