#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]

        for idx in range(2, len(dp)):
            dp[idx] = min(dp[idx -1] + cost[idx], dp[idx-2] + cost[idx])

        return min(dp[-1], dp[-2])
# @lc code=end
s  = Solution()
print(s.minCostClimbingStairs([0,2,2,1]))
