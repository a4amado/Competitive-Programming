#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uniqie = set()
        for idx, item in enumerate(nums):
            uniqie.add(item)
        nums_ = [x for x in uniqie]
        for i in range(len(nums) - len(uniqie)):
            nums_.append("_")
        nums_.sort()
        for i in range(len(nums_)):
            nums[i] = nums_[i]
        return len(uniqie)

# @lc code=end

