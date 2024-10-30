#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

from typing import List

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        for i in range(1, len(nums)):
            self.prefix[i] = self.prefix[i -1] + nums[i -1]
        self.suffex = [0] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            self.prefix[i] = self.prefix[i + 1] + nums[i + 1]
        self.total =sum(nums)
    def sumRange(self, left: int, right: int) -> int:
        return self.total - (self.prefix[left] + self.suffex[right])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

