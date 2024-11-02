#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}

        def recursion(idx: int, remaining: int, holding: bool):
            if idx >= len(prices) or remaining == 0:return 0
            if (idx, remaining, holding) in memo: return memo[(idx, remaining, holding)]

            skip = recursion(idx + 1, remaining, holding)
            if holding:
                sell = prices[idx] + recursion(idx + 1, remaining - 1, False)
            
                memo[(idx, remaining, holding)] = max(skip, sell)
            else:
                buy = -prices[idx] + recursion(idx + 1, remaining, True)
                memo[(idx, remaining, holding)] = max(skip, buy)
            
            return memo[(idx, remaining, holding)]

        return recursion(0, k, False)
            
# @lc code=end

k = 2
prices = [2,4,1]

sol = Solution()

print(sol.maxProfit(k, prices))