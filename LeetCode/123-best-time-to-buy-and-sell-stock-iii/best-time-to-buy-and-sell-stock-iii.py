from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize memoization dictionary
        memo = {}
        
        def recursion(idx: int, holding: bool, remaining: int) -> int:
            # Base case: if we've reached the end of the array
            if idx >= len(prices) or remaining <= 0:
                return 0
            
            # If we've seen this state before, return memoized result
            if (idx, holding, remaining) in memo:
                return memo[(idx, holding, remaining)]
            
            # Skip this day (always a valid choice)
            skip = recursion(idx + 1, holding, remaining)
            
            if holding:
                # If we're holding stock, we can sell
                # Profit = current price + future profits
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