#
# @lc app=leetcode id=2789 lang=python
#
# [2789] Largest Element in an Array after Merge Operations
#

# @lc code=start
from operator import le


class Solution(object):
    def __init__(self):
        self.num = 0

    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        for i in range(len(nums) - 2, 0, -1):
            if nums[i] > nums[i - 1]:
                sum = sum + nums[i] + nums[i - 1]
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                nums.pop()
        return nums[1]


s = Solution()
print(s.maxArrayValue([2, 3, 7, 9, 3]))
# @lc code=end
