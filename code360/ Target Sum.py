from collections import *
from math import *

from typing import List

def countPartitions(d: int, arr: List[int]) -> int:
    total = sum(arr)
    if (total - d) % 2 != 0 or total < d:
        return 0
    target = (total - d) // 2

    

    # def count_subsets(idx: int, curr_sum: int) -> int:
    #     # Base case
    #     if idx == n:
    #         return 1 if curr_sum == 0 else 0

    #     # Check memoization
    #     if (idx, curr_sum) in memo:
    #         return memo[(idx, curr_sum)]

    #     # Recursive cases
    #     not_take = count_subsets(idx + 1, curr_sum)
    #     take = 0
    #     if arr[idx] <= curr_sum:
    #         take = count_subsets(idx + 1, curr_sum - arr[idx])

    #     # Store result in memo and return
    #     memo[(idx, curr_sum)] = (take + not_take) % MOD
    #     return memo[(idx, curr_sum)]

    # return count_subsets(0, target)
    dp = [[0 for i in range(target + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(dp)):
        dp[i][0] = 1

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            # Recursive cases
            dp[i][j] = dp[i - 1][j]
            
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] + dp[i - 1][j - arr[i - 1]]
    return dp[-1][target]


def targetSum(arr: List[int], target: int) -> int:
    # memo = {}
    # def d(idx: int, sum:int):

    #     if idx == len(arr):
    #         if sum == target:return 1
    #         return 0

    #     key = (idx, sum)
        
    #     if key in memo: return memo[key]

    #     positiv = d(idx + 1, sum + arr[idx])
    #     negativ = d(idx + 1, sum - arr[idx])

    #     memo[key] = positiv + negativ
    #     return memo[key]
    # return d(0, 0)
    return countPartitions(target, arr)
   

ARR = [1, 1, 1, 1, 1]
TARGET = 3
print(
    targetSum(ARR, TARGET)
)