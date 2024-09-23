#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid  = (l + r) // 2
        while l <= r:
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid  = (l + r) // 2
        return - 1
        
# @lc code=end

