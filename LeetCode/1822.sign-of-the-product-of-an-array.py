#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

from typing import *
import math

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = math.prod(nums)
        if product == 0: return 0
        if product > 0: return 1
        return -1
# @lc code=end

