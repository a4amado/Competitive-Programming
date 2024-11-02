#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from typing import List

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        for idx, num in enumerate(nums, start=1):
            if idx != num:
                return [num, idx]
        return []

# @lc code=end

nums = [3,2,3,4,6,5]
sol = Solution()
print(sol.findErrorNums(nums))