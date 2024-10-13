from typing import *

def countWaysToMakeChange(denominations: List[int], value: int):
    
    memo = {}
    def power(idx: int, remaining:int):
        if remaining == 0:
            return 1
        if idx == len(denominations):
            return 0
        key = (idx, remaining)
        if key in memo: return memo[key]
        noTake = power(idx + 1, remaining)
        take = 0
        if denominations[idx] <= remaining:
            take = power(idx, remaining - denominations[idx])
        memo[key] =  noTake + take
        return memo[key]
    # return power(0, value)
    dp = [[0 for i in range(value + 1)] for i in range(len(denominations) + 1)]

    for i in range(len(dp)):
        dp[i][0] = 1
    
    for idx in range(1, len(dp)):
        for remaining in range(1, value + 1):
            dp[idx][remaining] = dp[idx  -1 ][remaining]
            if denominations[idx - 1] <= remaining:
                dp[idx][remaining] +=  dp[idx][remaining - denominations[idx -1]]
    return dp[-1][-1]



print(
    countWaysToMakeChange(
        [1, 2, 3], 4
    )
)
# returning 3 buit hosuld be 4

print(
    countWaysToMakeChange(
        [1, 2], 4
    )
)
