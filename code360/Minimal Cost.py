from typing import *

def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    memo = {}
    def recur(idx: int):
        if idx == n - 1: return 0
        if idx in memo: return memo[idx]

        min_cost = float('inf')

        for i in range(idx + 1, min(idx + k + 1, n)):
            cost = abs(heights[idx] - heights[i]) + recur(i)
            min_cost = min(cost, min_cost)
        
        memo[idx] = min_cost
        
        return memo[idx]
    return recur(0)




n = 3 
k = 1
height = [2, 5, 2]

print(
    minimizeCost(n, k,height )
)