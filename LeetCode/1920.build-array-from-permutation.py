#
# @lc app=leetcode id=1920 lang=python
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [_ for _ in range(len(nums))]
        for idx in range(len(nums)):
             ans[idx] = nums[nums[idx]]
        return ans

# @lc code=end

