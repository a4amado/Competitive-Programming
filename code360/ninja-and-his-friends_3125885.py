from os import *
from sys import *
from collections import *
from math import *
from typing import Dict, List, Tuple

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    def dfs(row: int, a: int, b: int, memo: Dict) -> int:
        if row >= len(grid):
            return 0
        
        if (row, a, b) in memo: return memo[(row, a, b)]

        curr = float('-inf')
        for idx in range(max(0, a-1), min(len(grid[row]), a+2)):
            for jdx in range(max(0, b-1), min(len(grid[row]), b+2)):
                next_val = dfs(row + 1, idx, jdx, memo)
                chocolates = grid[row][a] + (grid[row][b] if a != b else 0)
                curr = max(curr, next_val + chocolates)

        memo[(row, a, b)] = curr
        return curr
    memo = {}
    s = dfs(0, 0, len(grid[0]) - 1, memo)
    print(memo)
    return s

# Test the function
print(maximumChocolates(3, 4, [
    [2, 3, 1, 2],
    [3, 4, 2, 2],
    [5, 6, 3, 5]
]))



# print(
#     maximumChocolates(0,0, [[2,3,1,2],
# [3,4,2,2],
# [5,6,3,5]])
# )



# print(
#     maximumChocolates(0,0, 
#                       [[2,2],
# [1,1],
# [1,2]]
# )
# )



from typing import List

def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # Initialize a 3D DP table with dimensions (r x c x c)
    dp = [[[0] * c for _ in range(c)] for _ in range(r)]
    
    # Base case: fill the first row
    for a in range(c):
        for b in range(c):
            dp[0][a][b] = grid[0][a] + (grid[0][b] if a != b else 0)
    
    # Fill the DP table from the second row onwards
    for row in range(1, r):
        for a in range(c):
            for b in range(c):
                max_chocolates = -float('inf')
                
                # Explore all possible moves for both friends (move left, stay, or move right)
                for da in [-1, 0, 1]:
                    for db in [-1, 0, 1]:
                        na, nb = a + da, b + db
                        if 0 <= na < c and 0 <= nb < c:
                            chocolates = grid[row][a] + (grid[row][b] if a != b else 0)
                            max_chocolates = max(max_chocolates, dp[row-1][na][nb] + chocolates)
                
                dp[row][a][b] = max_chocolates
    
    # The result will be the maximum value in the last row for any (a, b) pair
    result = max(dp[r-1][a][b] for a in range(c) for b in range(c))
    return result

# Test the function
print(maximumChocolates(3, 4, [
    [2, 3, 1, 2],
    [3, 4, 2, 2],
    [5, 6, 3, 5]
]))
