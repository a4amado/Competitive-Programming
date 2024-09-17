from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[n - 1]



        # memo = {}

        # def dfs(num:int):
        #     if num == 0:
        #         return 0
        #     if num < 0:
        #         return float('inf')


        #     if num in memo:
        #         return memo[num]

        #     min_coins = float('inf')
        #     for i in coins:
        #         if i <= num:
        #             c = dfs(num - i)
        #             if c != float('inf'):
        #                 stepsHereTillTheEnd = c + 1
        #                 min_coins = min(stepsHereTillTheEnd, min_coins)
                    

        #     memo[num] = min_coins
        #     return min_coins
        # res = dfs(amount)
        # return res if res != float('inf') else - 1

s = Solution()
print(s.coinChange([1,2,5], 3))