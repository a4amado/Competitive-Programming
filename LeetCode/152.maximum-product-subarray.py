#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]

        for i in range(1, n):
            
            # The max could be one of three
            # 1. the currunt item
            # 2. the currunt item multiplied by the currMax
            # 3. the currunt item multiplied by the currMin
            newMax = max(nums[i], nums[i] * currMax, nums[i] * currMin)

            # The min could be one of three
            # 1. the currunt item
            # 2. the currunt item multiplied by the currMax
            # 3. the currunt item multiplied by the currMin
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)

            currMax = newMax

            maxProd = max(maxProd, currMax)
        return maxProd

# @lc code=end

