from os import *
from sys import *
from collections import *
from math import *

from typing import List

def minimumElements(nums: List[int], x: int) -> int:
    memo = {}
    def d(idx: int , remainging: int):
        if remainging == 0:
                return 0
        if idx == len(nums):
            return float('inf')
        
        if (idx, remainging)  in memo: return memo[(idx, remainging)]
        
        notTake = d(idx + 1, remainging)
        take = float('inf')
        if nums[idx] <= remainging:
            take = d(idx, remainging - nums[idx]) + 1
        
        memo[(idx, remainging)] = min(take, notTake)
        return memo[(idx, remainging)]
    result = d(0, x)
    return result if result != float('inf') else -1

    dp = [[float('inf') for _ in range(x + 1)] for _ in range(len(nums) + 1)]
    
    # Base case: to make 0 amount, 0 coins are needed
    for i in range(len(nums) + 1):
        dp[i][0] = 0

    # Fill the dp table
    for i in range(1, len(nums) + 1):
        for j in range(1, x + 1):
            # Exclude the coin
            dp[i][j] = dp[i - 1][j]
            
            # Include the coin if it's less than or equal to j
            if nums[i - 1] <= j:
                dp[i][j] = min(dp[i][j], dp[i][j - nums[i - 1]] + 1)

    # If the target cannot be reached, return -1
    return dp[len(nums)][x] if dp[len(nums)][x] != float('inf') else -1

print(
    minimumElements([1,2,3],  7)
)

print(
    minimumElements([12, 1, 3] , 4 )
)
