#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefex_arr = [0]*len(nums)
        prefex_arr[0] = 1

        suffex_arr = [0]*len(nums)
        suffex_arr[-1] = 1

        
        for idx in range(1, len(nums)):
            prefex_arr[idx] = prefex_arr[idx-1] * nums[idx - 1]
        
        for idx in range(len(nums) - 2 , -1, -1):
            suffex_arr[idx] = suffex_arr[idx + 1] * nums[idx + 1]

        res = [0]*len(nums)

        for i in range(len(res)):
            res[i] = prefex_arr[i] * suffex_arr[i]
        return res
# @lc code=end

