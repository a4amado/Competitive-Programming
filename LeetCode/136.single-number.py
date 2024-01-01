#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()

        for i in range(0, len(nums) -1):
            if i == 0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            else:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    return nums[i]
                
        return nums[-1]
s = Solution()
# @lc code=end

