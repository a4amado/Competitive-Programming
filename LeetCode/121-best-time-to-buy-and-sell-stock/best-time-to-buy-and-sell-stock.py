class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_after = [float('-inf')] * len(prices)

        max_til_now = prices[-1]
        max_after[-1] = prices[-1]

        for idx in range(len(prices) -2, -1, -1):
            max_after[idx] = max_til_now
            max_til_now = max(max_til_now, prices[idx])
        
        max_diff = 0

        for i in range(len(prices)):
            if max_after[i] >  prices[i]:
                max_diff = max(max_diff, max_after[i] -  prices[i])
        return max_diff