#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

from typing import List
import bisect

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]
        # an
        for num in nums[1:]:
            if num  > dp[-1]:
                dp.append(num)
            else:
                idx = bisect.bisect_left(dp, num)
                dp[idx] = num
          
        return dp
# @lc code=end
s = Solution()
print(s.lengthOfLIS([0,1,0,3,2,3]))
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(s.lengthOfLIS(arr))