# #
# # @lc app=leetcode id=518 lang=python3
# #
# # [518] Coin Change II
# #
# from typing import *

# # @lc code=start
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         total = sum(coins)
#         def d(idx: int, remaining: int, memo: Dict):
#             if remaining == 0: return 1
#             if idx == len(coins): return 0
#             key = (idx, remaining)
#             if key in memo: return memo[key]
#             notTake = d(idx+ 1, remaining, memo)
#             take = 0
#             if coins[idx] <= remaining:
#                 take = d(idx, remaining - coins[idx], memo)
#             memo[key] = notTake + take
#             return memo[key]
#         # return d(0, amount, {})
#         dp = [
#             [
#                 0 for i in range(amount + 1)
#             ] for _ in range(len(coins) + 1)
#         ]
#         for i in range(len(dp)):
#             dp[i][0] = 1
        
#         for idx in range(1, len(dp)):
#             for remaining in range(0, len(dp[0])):
#                 dp[idx][remaining] = dp[idx - 1][remaining]
#                 if coins[idx -1] <= remaining:    
#                     dp[idx][remaining] = dp[idx][remaining] + dp[idx][remaining - coins[idx -1]]
#         return dp[-1][-1]
# # @lc code=end

from typing import List, Dict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        def d(idx: int, remaining: int, memo: Dict):
            if remaining == 0: return 1
            if idx == len(coins): return 0

            key = (idx, remaining)		
            if key in memo: return memo[key]
            # notTake
            noTake = d(idx+1, remaining, memo)
            take = 0
            if coins[idx] <= remaining:
                take = d(idx, remaining - coins[idx], memo)
            memo[key] = take + noTake
            return memo[key]
            
        return d(0, amount, {})

amount = 5
coins = [1,2,5]

s = Solution()
print(
    s.change(amount, coins)
)