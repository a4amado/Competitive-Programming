#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

from typing import List


# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        low = 0
        high = low + 1

        if nums[high] < nums[low]:
            high, low = low,  high

        for i in range(2, len(nums)):
            if nums[i] > nums[high]:
                low = high
                high = i
            elif nums[i] > nums[low]:
                low = i

        if nums[high] >= nums[low] * 2:
            return high
        return -1
# s= Solution()

# print(s.dominantIndex([3,6,1,0]))


# @lc code=end
