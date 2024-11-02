#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def recursion(idx: int, holding: bool):
            if idx >= len(prices):return 0

            if (idx, holding) in memo: return memo[(idx, holding)]

            skip  = recursion(idx + 1, holding)
            if holding:
                sell = prices[idx] + recursion(idx + 2, False)
                memo[(idx, holding)] = max(sell, skip)
            else:
                buy = -prices[idx] + recursion(idx + 1, True)
                memo[(idx, holding)] = max(buy, skip)
            return memo[(idx, holding)]
        
        return recursion(0, False)

# @lc code=end

