#
# @lc app=leetcode id=1512 lang=python
#
# [1512] Number of Good Pairs
#
from typing import *
from collections import Counter


# @lc code=start
class Solution(object):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        def n(i: int):
            return i * (i-1) / 2
        num = 0
        for val in count.values():
            num += n(val)
        return int(num)
        
        
# @lc code=end


nums = [1,2,3,1,1,3]

sol = Solution()
print(sol.numIdenticalPairs(nums))

nums = [1,1,1,1]
print(sol.numIdenticalPairs(nums))