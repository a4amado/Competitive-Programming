#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

from typing import List

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) -1
        mid = (l + r) // 2
        while l < r:
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
            mid = (l + r) // 2
        return nums[l]
# @lc code=end

s = Solution()
print(s.findMin([3,4,5,1,2]))
print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin( [11,13,15,17]))
