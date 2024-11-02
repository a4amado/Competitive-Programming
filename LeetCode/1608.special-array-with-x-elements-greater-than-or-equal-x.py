#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

from typing import List
import collections

# @lc code=start
# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Include max(nums) in the range
        d = {
            idx: 0 for idx in range(max(nums) + 1)
        }
        
        # Count numbers greater than or equal to each index
        for idx in nums:
            for i in range(idx + 1):
                d[i] += 1

        # Check for special value
        for idx, count in d.items():
            if idx == count:  # Changed condition
                return idx
        return -1
    
# @lc code=end



nums = [3,5]

sol = Solution()

print(sol.specialArray(nums))
nums = [0,0]

print(sol.specialArray(nums))
nums = [0,4,3,0,4]
print(sol.specialArray(nums))