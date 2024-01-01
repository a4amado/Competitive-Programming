#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros  = 0
        l = len(nums)
        i = 0
        while i < l - zeros:
            if nums[i] == 0:
                del nums[i]
                zeros = zeros  + 1
            else:
                i = i + 1
        for i in range(zeros):
            nums.append(0)
        return nums
# @lc code=end


