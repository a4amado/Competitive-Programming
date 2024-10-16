#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

from typing import *

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        l = 0
        r = 0

        allTimeLongest = 0
        while True:
            if l >= len(nums) or r >= len(nums): break
            diff = abs(nums[l] - nums[r])
            if diff <= limit:
                r += 1
            else:
                r += 1
                l += 1
            allTimeLongest = max(allTimeLongest,abs(r - l))
        
        return allTimeLongest
            
# @lc code=end

s = Solution()
nums = [1,5,6,7,8,10,6,5,6]

limit = 5 
print(s.longestSubarray(nums, limit))
