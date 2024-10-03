#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

from typing import *

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c = image[sr][sc]
        def dfs(row:int, col: int, visited: List[List[int]]):
            # if out of bound 
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]): return
            # if not the same color
            if image[row][col] != c:return
            # is visited
            if visited[row][col]:return

            visited[row][col] = True

            image[row][col] = color
            dfs(row + 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row - 1, col, visited)
            dfs(row, col - 1, visited)
        visited = [[False for i in range(len(image[0]))]  for i in range(len(image))]
        dfs(sr, sc, visited)
        return image
            
            
            
s = Solution()
print(
    s.floodFill([[1,1,1],
                 [1,1,0],
                 [1,0,1]], 1, 1, 2)
)

# @lc code=end

# Input: image = [[1,1,1],
#                 [1,1,0],
#                 [1,0,1]
# ], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]