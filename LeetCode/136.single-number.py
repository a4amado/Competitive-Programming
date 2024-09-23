#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

from collections import Counter
# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = Counter(nums)
        for i in count:
            if count[i] == 1:
                return i
            
                
s = Solution()
# @lc code=end

print(s.singleNumber([3,2,3]))