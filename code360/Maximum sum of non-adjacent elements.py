# https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261

from os import *
from sys import *
from collections import *
from math import *
from typing import *
from sys import stdin

def maximumNonAdjacentSum(nums: List[int]) -> int:
    # memo = {}
    
    # def dfs(idx: int) -> int:
    #     if idx >= len(nums):
    #         return 0
    #     if idx in memo:
    #         return memo[idx]
        
    #     # Take current number
    #     take = nums[idx] + dfs(idx + 2)
        
    #     skip = dfs(idx + 1)
        
    #     memo[idx] = max(take, skip)
    #     return memo[idx]
    
    # return max(dfs(0), 0)  # Ensure the result is non-negative
    
    # Tabulization
    if len(nums) < 3:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]
    for i in range(3, len(nums)):
        twoStepsBack = dp[i - 2] + nums[i]
        threeStepsBack = dp[i - 3] + nums[i]
        dp[i]  = max(twoStepsBack, threeStepsBack )
    return max(dp)
# print(maximumNonAdjacentSum([1,2,4]))

print(maximumNonAdjacentSum([9,9,8,2]))
# print(maximumNonAdjacentSum([8,5,8,8]))

# print(maximumNonAdjacentSum([1, 2, 4]))
# print(maximumNonAdjacentSum([2, 1, 4, 9]))

# Main.
# t = int(stdin.readline().rstrip())

# while t > 0:
    
#     n = int(stdin.readline().rstrip())
#     arr = list(map(int, stdin.readline().rstrip().split(" ")))
#     print(maximumNonAdjacentSum(arr))
    
#     t -= 1