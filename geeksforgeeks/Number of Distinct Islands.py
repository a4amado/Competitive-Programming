#User function Template for python3

import sys
from typing import *
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:

        def dfs(row:int, col: int, visited: Dict, topolgicalList: List[Tuple[int]]):
            if not (0 <= row < len(grid) and 0 <= col <len(grid[0])):
                return
            if (row, col) in visited:return
            visited[(row, col)] = True
            if grid[row][col] == 0: return

            dfs(row+1, col, visited, topolgicalList)
            dfs(row-1, col, visited, topolgicalList)
            dfs(row, col+1, visited, topolgicalList)
            dfs(row, col-1, visited, topolgicalList)

            topolgicalList.append((row, col))
        
        final = []
        visited = {}
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                l = []
                if (row, col) not in visited:
                    dfs(row, col, visited, l)
                    if l:
                        final.append(l)

        
        
        unqie = set()
        for _, shape in enumerate(final):
            relativePoint = shape[0]
            aa = []
            for _, point in enumerate(shape):
                y, x = point[0] - relativePoint[0], point[1] - relativePoint[1]
                aa.append((y, x))
            unqie.add(tuple(aa))
        return len(unqie)
            


# grid = [
#         [1, 1, 0, 0, 0],
#         [1, 1, 0, 0, 0],
#         [0, 0, 0, 1, 1],
#         [0, 0, 0, 1, 1]
# ]


grid2 = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

s = Solution()
s.countDistinctIslands(grid2)