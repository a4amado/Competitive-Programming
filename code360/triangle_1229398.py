# https://www.naukri.com/code360/problems/triangle_1229398?leftPanelTabValue=PROBLEM

from os import *
from sys import *
from collections import *
from math import *
from typing import *
import copy

def minimumPathSum(triangle: List[List[int]], n: int):
    # def dfs(row:int, col: int, memo: Dict[(int, int)]):
    #     if row >= len(triangle):return float('inf')
    #     if col >= len(triangle[row]):return float('inf')

    #     if (row, col) in memo: return memo[(row, col)]
        
    #     if (row + 1 == len(triangle)):
    #         return triangle[row][col]
        
        
    #     memo[(row, col)] = min(dfs(row + 1, col, memo), dfs(row + 1, col  + 1, memo)) + triangle[row][col]

    #     return memo[(row, col)]
    # memo = {}
    # return dfs(0,0, memo)

    def forReal(row:int, col: int):
        if row >= len(triangle) or row < 0:return float('inf')
        if col >= len(triangle[row]) or col < 0:return float('inf')
        return dp[row][col]

    dp = copy.deepcopy(triangle)

    for idx in range(1, len(dp)):
        for jdx in range(len(triangle[idx])):
            dp[idx][jdx] = triangle[idx][jdx]  + min(forReal(idx - 1, jdx), forReal(idx - 1, jdx  - 1))
    return min(dp[-1])


print(
    minimumPathSum([
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
], 0)
)


# [
#     [2],
#     [3,4],
#     [6,5,7],
#     [4,1,8,3]
# ]
