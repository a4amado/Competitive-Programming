#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = {}
        for idx,  item in enumerate(nums):
            if s.get(item) == None:
                s[item] = True
            else:
                return True


# @lc code=end

