#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

from typing import List

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# @lc code=end
s = Solution()
s.lengthOfLIS([0,1,0,3,2,3])