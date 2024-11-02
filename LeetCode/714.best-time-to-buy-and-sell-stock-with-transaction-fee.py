#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}


        def dp(idx: int, holding: bool):
            if idx >= len(prices): return 0
            key = (idx, holding)
            if key in memo: return memo[key]
            
            

            skip = dp(idx  + 1, holding)
            if holding:
                sell = (prices[idx] - fee) + dp(idx + 1, False)
                memo[key] = max(skip, sell)
            else:
                buy = -prices[idx] + dp(idx + 1, True)
                memo[key] = max(buy, skip)
            return memo[key]
        
        return dp(0, False)

# @lc code=end

