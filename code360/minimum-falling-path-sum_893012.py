from os import *
from sys import *
from collections import *
from math import *
from typing import *
from sys import stdin, setrecursionlimit
import copy

setrecursionlimit(10**7)


def getMaxPathSum(matrix: List[List[int]]):


    dp = copy.deepcopy(matrix)

    for row in range(1, len(matrix)):
        for col in range(len(matrix[row])):
            before = float('-inf') if col <= 0 else dp[row-1][col-1]
            above = dp[row-1][col]
            after = float('-inf') if col+1 >= len(dp[row]) else dp[row-1][col+1]
            dp[row][col] = max(before + dp[row][col], above + dp[row][col], after+dp[row][col])
    return max(dp[-1])





 



    # def dfs(row: int, col: int, memo: Dict[(int, int)]):
    #     if row >= len(matrix): return float('-inf')
    #     if col >= len(matrix[0]) or col < 0: return float('-inf')
        
    #     if (row, col) in memo: return memo[(row, col)]

    #     m = max(
    #         dfs(row+1, col +1, memo),
    #         dfs(row+1, col, memo),
    #         dfs(row+1, col - 1, memo)
    #     )
    #     memo[(row, col)] = matrix[row][col] + max(0, m)
        
    #     return memo[(row, col)]
    
    # minTilNow = float('-inf')
    # memo = {}
    # for idx, val in enumerate(matrix[0]):
    #     memo[(0, idx)] = max(minTilNow, dfs(0, idx, memo))
    #     minTilNow = memo[(0, idx)]

    # return minTilNow



# print(getMaxPathSum([
#                         [1,2,10,4],
#                         [100,3,2,1],
#                         [1,1,20,2],
#                         [1,2,2,1]
#                     ]))


# print(getMaxPathSum([
#                         [10,2,3],
#                         [3,7,2],
#                         [8,1,5]
#                     ]))


print(getMaxPathSum(
    [[1,2,10,4],
[100,3,2,1],
[1,1,20,2],
[1,2,2,1]

]
))

        
              
