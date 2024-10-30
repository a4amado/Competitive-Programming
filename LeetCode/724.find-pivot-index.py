#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        for i in range(len(nums)):
            if prefix[i] == suffix[i]: return i
        return -1
# @lc code=end

