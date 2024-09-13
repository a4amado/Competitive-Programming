#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                if matrix[0][i] == 0:
                    for i in range(len(matrix[0])):
                        matrix[0][i] = 0
                    return
        if len(matrix) == 0:
                    return
        
        maxRows = len(matrix)
        maxCols = len(matrix[0])

        
        shouldZeroFirstRow = False
        shouldZeroFirstCol = False

        for row in range(maxRows):
            for col in range(maxCols):
                currItem = matrix[row][col]
                if currItem == 0:
                    if col == 0 and row == 0:
                        shouldZeroFirstRow = True
                        shouldZeroFirstCol = True
                    elif col == 0 or row == 0:
                        if col == 0:
                            shouldZeroFirstCol = True
                            matrix[row][0] = 0
                        else:
                            shouldZeroFirstRow = True
                            matrix[0][col] = 0
                    else:
                        matrix[0][col] = 0
                        matrix[row][0] = 0
        
        for row in range(1, maxRows):
            for col in range(1, maxCols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if shouldZeroFirstRow:
            for col in range(maxCols):
                matrix[0][col] = 0

        if shouldZeroFirstCol:
            for row in range(maxRows):
                matrix[row][0] = 0


        
# @lc code=end

s= Solution()
ss = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(ss)
print(ss)


