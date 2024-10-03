from os import *
from sys import *
from collections import *
from math import *
from typing import *

# def subsetSumToK(n, k, arr: List[int]):
#     memo = {}
#     def backtracking(idx: int, curr: int):
#         if curr == 0: return True

#         if (idx < 0) or (curr < 0): return False
#         if (idx, curr) in memo: return memo[(idx, curr)]
        
#         take = backtracking(idx - 1, curr - arr[idx] )
        
#         if curr <= arr[idx]:
#             notTake = backtracking(idx - 1, curr)
        
#         memo[(idx, curr)] = take or notTake
#         return memo[(idx, curr)]

#     return backtracking(len(arr) - 1, k)

from typing import List

def subsetSumToK(n: int, k: int, arr: List[int]) -> bool:
    # Initialize dp table: dp[i][j] will be True if there is a subset
    # of the first i elements that sums to j.
    dp = [[False for _ in range(k + 1)] for _ in range(n + 1)]

    # Base case: a sum of 0 can always be achieved with an empty subset
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # Exclude the current element
            dp[i][j] = dp[i - 1][j]
            
            # Include the current element if it is not larger than j
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    # Return whether the subset that sums to k exists
    return dp[n][k]


# def subsetSumToK(n, k, arr):
#     # Create a DP table of size (n+1) x (k+1)
#     dp = [[False] * (k + 1) for _ in range(n + 1)]

#     # There's always a way to form sum 0 (by taking no elements)
#     for i in range(n + 1):
#         dp[i][0] = True

#     # Fill the table
#     for i in range(1, n + 1):
#         for j in range(1, k + 1):
#             # If the current element is not included
#             dp[i][j] = dp[i - 1][j]

#             # If the current element can be included
#             if arr[i - 1] <= j:
#                 dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

#     # The answer will be in dp[n][k]
#     return dp[n][k]


print(subsetSumToK(5,4, [2, 5, 1, 6, 7]))
# print(subsetSumToK(0,4, [2,5,1,6,7]))

    
    
    

# print(subsetSumToK(0, 5, [4,3,2,1]))
# print(subsetSumToK(0, 4, [2,5,1,6,7]))
# print(subsetSumToK(0, 4, [6,1,2,1]))
# print(subsetSumToK(0, 6, [1,7,2,9,10]))

