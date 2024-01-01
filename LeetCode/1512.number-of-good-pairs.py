#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = 0
        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] == nums[j]:
                    dic = dic + 1
        return dic
# @lc code=end