#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

from typing import *

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # is increaing
        isIncreasing = True
        for idx in range(len(nums) -1):
            first = nums[idx]
            other = nums[idx + 1]
            if first > other:
                isIncreasing = False
                break

        if isIncreasing: return isIncreasing
        isDecreasing = True
        for idx in range(len(nums) -1):
            first = nums[idx]
            other = nums[idx + 1]
            if first < other:
                isDecreasing = False
                break
        if isDecreasing: return isDecreasing
        return False
# @lc code=end

