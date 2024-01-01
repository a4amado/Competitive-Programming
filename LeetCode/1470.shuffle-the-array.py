#
# @lc app=leetcode id=1470 lang=python
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[n + i])
        return l
# @lc code=end

