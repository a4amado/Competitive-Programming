#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

from typing import List

# @lc code=start

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        memo = {}
        # [1,2,3,1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for idx in range(2, len(nums)):
            dp [idx] = max(nums[idx] + dp[idx-2], nums[idx] + dp[idx-3])

        # def dfs(i:int):
        #     if i >= len(nums):return 0
        #     if i in memo:return memo[i]
        #     memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
        #     return memo[i]
        
        # return dfs(0)
        return max(dp)
        
# @lc code=end
s = Solution()

print(s.rob([1,2,3,1]))