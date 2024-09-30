from typing import *

def minSumPath(grid: List[List[int]]):
    rows, cols = len(grid), len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = grid[0][0]
    # prepare first row
    for i in range(1, cols):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, rows):
        
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
    return dp[-1][-1]
        
print(minSumPath([[5, 9, 6],[11,5,2]]))
print(minSumPath([[1,2,3],
[4,5,4],
[7,5,9]]))

