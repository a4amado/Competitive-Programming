#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

from typing import List

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()

        return (nums[-1] * nums[-2]) - (nums[1] * nums[0])
        
# @lc code=end

