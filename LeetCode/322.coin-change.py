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


from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # If amount is 0, no coins are needed
        if amount == 0:
            return 0
        
        coins.sort(reverse=True)
 
        # Initialize the queue with the starting amount 0 and 0 coins used
        queue = deque([(0, 0)])  # (current amount, number of coins)
        
        visited = {0,0}
        
        while queue:
            curr_amount, num_coins = queue.popleft()
            
            for coin in coins:
                newAmount = curr_amount + coin
                if newAmount == amount:
                    return num_coins + 1
                
                if newAmount > amount:
                    continue

                if newAmount not in visited or num_coins + 1 < visited[newAmount]:
                    visited.add(newAmount, num_coins + 1)
                    queue.append((newAmount, num_coins + 1))
                
                
                
            
        
        # If we exit the loop without returning, the amount cannot be formed
        return -1
