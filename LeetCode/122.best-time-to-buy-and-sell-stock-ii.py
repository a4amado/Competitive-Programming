from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        # Create arrays to track max profit with and without holding stock
        # curr[0] is profit without stock, curr[1] is profit while holding
        curr = [0, -prices[0]]  # Initial state
        
        # Fill the dp table
        for i in range(1, n):
            prev_no_stock = curr[0]
            prev_with_stock = curr[1]
            
            # If not holding stock on day i, either keep not holding or sell
            curr[0] = max(prev_no_stock, prev_with_stock + prices[i])
            
            # If holding stock on day i, either keep holding or buy
            curr[1] = max(prev_with_stock, prev_no_stock - prices[i])
        
        # Return max profit without holding stock on last day
        return curr[0]