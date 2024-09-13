#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

from typing import List, Literal

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l: List[int] = []
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        def dfs(y: int,x: int, currDir: Literal["r" , "l" , "d" , "u"], l: List[int]):
            if len(l) == len(matrix) * len(matrix[0]):
                return l
            l.append(matrix[y][x])
            visited[y][x] = True
            if currDir == "r":
                if x < len(matrix[0]) - 1 and not visited[y][x + 1]:
                    dfs(y, x + 1, currDir, l)
                else:
                    dfs(y + 1, x, "d", l)
            elif currDir == "d":
                if y < len(matrix) - 1 and not visited[y + 1][x]:
                    dfs(y + 1, x, "d", l)
                else:
                    dfs(y, x - 1, "l", l)
            elif currDir == "l":
                if x > 0 and  not visited[y][x - 1]:
                    dfs(y, x - 1, "l", l)
                else:
                    dfs(y - 1, x, "u", l)
            elif currDir == "u":
                if y > 0 and  not visited[y - 1][x]:
                    dfs(y - 1, x, "u", l)
                else:
                    dfs(y, x + 1, "r", l)
        dfs(0,0,"r", l)                
        return l


# @lc code=end
s = Solution()
print(s.spiralOrder([[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]))
