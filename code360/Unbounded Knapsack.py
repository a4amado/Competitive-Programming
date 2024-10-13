from typing import *


def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:
    
    def d(idx:int, remaining: int, memo: Dict):
        if idx == n or remaining == 0:return 0
        
        

        key = (idx, remaining)
        if key in memo: return memo[key]

        noTake = d(idx + 1, remaining, memo)
        take = 0
        if weight[idx] <= remaining:
            take = d(idx, remaining - weight[idx], memo) + profit[idx]
        
        memo[key] = max(take, noTake)
        
        return memo[key]
    memo = {}
    # return d(0, w, memo)
    dp = [[0 for i in range(w + 1)] for _ in range(n + 1)]
    
    prev = [0 for i in range(w + 1)]
    curr = [0 for i in range(w + 1)]

    for idx in range(1, len(dp)):
        for remaining in range(len(dp[idx])):
            curr[remaining] = prev[remaining]

            if weight[idx - 1] <= remaining:
                curr[remaining] = max(curr[remaining], curr[remaining - weight[idx - 1]] + profit[idx - 1])
        prev = curr
        curr = [0 for i in range(w + 1)]              
    return max(prev)

n = 6
w = 7
profit = [8, 5, 3, 6, 4, 9]
weight = [5, 3, 6, 8, 7, 4]
print(
    unboundedKnapsack(n,w,profit, weight)
) # prints 10 but it suppose to return 14



# n = 3
# w = 10
# profit = [5, 11, 13]
# weight = [2, 4, 6]

# print(
#     unboundedKnapsack(n,w,profit, weight)
# )