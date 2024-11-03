#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#

from typing import List

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[float('inf') for i in range(cols)]for i in range(rows)]
        dp[0] = matrix[0][:]
        
        dirs = [-1,0,1]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                for dx in dirs:
                    new_col = j + dx
                    if not (0 <= new_col < len(matrix[0])):continue
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i-1][new_col] )
        return min(dp[-1])


# @lc code=end


matrix = [[2,1,3],[6,5,4],[7,8,9]]

sol = Solution()
print(sol.minFallingPathSum(matrix))

matrix = [[-19,57],[-40,-5]]

print(sol.minFallingPathSum(matrix))
