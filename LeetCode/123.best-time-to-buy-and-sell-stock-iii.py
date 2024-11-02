#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize memoization dictionary
        memo = {}
        dp = [[[0,0] for _ in range(3)] for _ in range(prices)]

        
        def recursion(idx: int, holding: bool, remaining: int) -> int:
            # Base case: if we've reached the end of the array
            if idx >= len(prices) or remaining == 0:
                return 0
            
            # If we've seen this state before, return memoized result
            if (idx, holding, remaining) in memo:
                return memo[(idx, holding, remaining)]
            
            # Skip this day (always a valid choice)
            skip = recursion(idx + 1, holding, remaining)
            
            if holding:
                # If we're holding stock, we can sell
                # Profit = current price + future profits
                sell.asd
                sell = prices[idx] + recursion(idx + 1, False, remaining -1)
                memo[(idx, holding, remaining)] = max(skip, sell)
            else:
                # If we're not holding stock, we can buy
                # Cost = -current price + future profits
                buy = -prices[idx] + recursion(idx + 1, True,remaining)
                memo[(idx, holding, remaining)] = max(skip, buy)
                
            return memo[(idx, holding, remaining)]
        
        # Start recursion from day 0, not holding any stock
        return recursion(0, False, 2)
# @lc code=end

prices = [3,3,5,0,0,3,1,4]

sol = Solution()

prices(sol.maxProfit(prices))

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][j][k]: max profit on day i, with j transactions left, k holding (0: not holding, 1: holding)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]
        
        # Fill DP table from start to end
        for i in range(n):
            for j in range(2):  # Remaining transactions
                if i == 0:
                    # Base case initialization
                    dp[i][j][0] = 0  # If we do nothing on day 0
                    dp[i][j][1] = -prices[i]  # If we buy on day 0
                else:
                    # Not holding stock
                    dp[i][j][0] = max(dp[i - 1][j -1][0], dp[i - 1][j -1][1] + prices[i])
                    # Holding stock
                    dp[i][j][1] = max(dp[i - 1][j -1][1], dp[i - 1][j][0] - prices[i])

        # Answer is the max profit on the last day, with 2 transactions left, and not holding any stock
        return dp[n - 1][2][0]

# Example usage
prices = [3, 3, 5, 0, 0, 3, 1, 4]
sol = Solution()
print(sol.maxProfit(prices))
