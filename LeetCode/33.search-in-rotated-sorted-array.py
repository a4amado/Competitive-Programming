#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        
        left, right = 0, len(nums) - 1
        
        # find pivot
        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid


        
        start = left

        if  target  > nums[len(nums) - 1]:
            left = 0
            right = max(start - 1, 0)
        else:
            left = start
            right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # calculate mid index
            if nums[mid] == target:  # if target found
                return mid
            elif nums[mid] > target:  # if target is smaller, ignore the right half
                right = mid - 1
            else:  # if target is larger, ignore the left half
                left = mid + 1


        return -1

# @lc code=end

s = Solution()
s.search([4,5,6,7,0,1,2], 0)