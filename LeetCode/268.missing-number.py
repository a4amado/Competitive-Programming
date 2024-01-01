#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        curr_num = len(nums)
        missing_num = 0
        while missing_num is 0 and len(nums) != 0:
            if nums[len(nums) - 1] != curr_num:
                return curr_num
            else:
                nums.pop()
                curr_num = curr_num -1
        return 0
# @lc code=end

