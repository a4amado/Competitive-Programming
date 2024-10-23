#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
from typing import *

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            idx = abs(num) - 1
            
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]
            

        return res
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
            
        # Iterate through each number in the array
        for num in nums:
            # Get the absolute value since the number might be negative due to previous marking
            index = abs(num) - 1
            
            # If the number at index is negative, we've seen this number before
            if nums[index] < 0:
                result.append(abs(num))
            # Otherwise, mark it as seen by making it negative
            else:
                nums[index] = -nums[index]
        
        return result
# @lc code=end

nums = [4,3,2,7,8,2,3,1]

sol = Solution()

print(
    sol.findDuplicates(nums)
)

