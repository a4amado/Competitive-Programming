#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

from typing import *

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        count_deleted = 0
        while idx < len(nums):
            if val == nums[idx]:
                nums[idx], nums[-1] = nums[-1], nums[idx]
                nums.pop()
                count_deleted += 1
            else:
                idx += 1
