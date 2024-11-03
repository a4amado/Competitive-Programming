# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
from typing import List

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        currSum = 0
        right = 0
        count = 0
        left = 0

# @lc code=end

# Test the solution
nums = [1, 0, 1, 0, 1]
goal = 2

sol = Solution()
print(sol.numSubarraysWithSum(nums, goal))
