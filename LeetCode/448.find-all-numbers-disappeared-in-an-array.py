#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        i = 0
        should_be = 1
        l = []
        while i < len(nums):
            if nums[i] == should_be:
                i = i + 1
                should_be = should_be + 1
            elif nums[i] > should_be:
                l.append(should_be)
                should_be = should_be + 1
            else:
                i = i + 1
        while should_be <= len(nums):
            l.append(should_be)
            should_be = should_be + 1
        return l

# @lc code=end

