#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List

# @lc code=start

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        curr = nums[0]
        prev = 0

        # [1,2,3,1]
        for val in nums[1:]:
            new_max = prev + val
            prev = curr
            curr = max(new_max, curr)
        return max(curr, prev)

# @lc code=end
