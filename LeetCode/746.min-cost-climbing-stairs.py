#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp = [0] * len(cost)
        
        # dp[0] = cost[0]
        # dp[1] = cost[1]

        # for idx in range(2, len(dp)):
        #     dp[idx] = min(dp[idx -1] + cost[idx], dp[idx-2] + cost[idx])
        # return min(dp[-1], dp[-2])
        memo = {}
        def dfs(idx:int):
            if idx < 0:return 0

            if idx in memo:
                return memo[idx]
            one = dfs(idx-1) + (cost[idx] if idx < len(cost) else 0)
            two = dfs(idx-2) + (cost[idx] if idx < len(cost) else 0)
            memo[idx]= min(one, two)
            return min(one, two)

        return dfs(len(cost))
# @lc code=end
s  = Solution()
s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
