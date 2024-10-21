#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import *
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def parent(row: int, col: int):
            newRow = row -1
            left = col -1
            right = col 
            res = [newRow]
            if col == 0:
                res.append(0)
            elif col == row:
                res.append(col-1)
            else:
                res.append(left)
                res.append(right)
            return res

        pascal = [
            [1] * idx for idx in range(1, numRows + 1)
        ]
        for row in range(numRows):
            for col in range(row):
                parents = parent(row, col)
                if len(parents) < 3:
                    pascal[row][col] = 1
                else:
                    pascal[row][col] = pascal[parents[0]][parents[1]]  + pascal[parents[0]][parents[2]]
        return pascal

        
# @lc code=end

numRows = 5

sol = Solution()
print(sol.generate(numRows))
