#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(row:int, col: int, path: List[(int)], visited: List[List[int]]):
            if self.isOutOfRange(row, col, len(visited), len(visited[0])):
                return False

            if visited[row][col]:return False
            
            if row == len(visited) -1 and col == len(visited[0]) - 1: 
                
                return 1
            
            visited[row][col]= True
            path.append((row, col))
            l = dfs(row+1, col, path, visited)
            r= dfs(row, col +1, path, visited)

            path.pop()
            visited[row][col] = False
            return l + r
        
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        return dfs(0,0, [], visited)

        # dp = [[1 for x in range(n)] for _ in range(m)]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # return dp[m - 1][n - 1]
    def isOutOfRange(seld, row:int,  col:int, maxRow:int, maxCol: int):
        if row < 0:return True
        if col < 0:return True
        if row >= maxRow:return True
        if col >= maxCol:return True
        return False

s = Solution()
print(s.uniquePaths(3, 7))
# @lc code=end

