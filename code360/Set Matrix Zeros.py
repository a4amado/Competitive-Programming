from math import *
from collections import *
from sys import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    shouldtheFirstRowBeZeroed = False
    shouldtheFirstColBeZeroed = False


    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            shouldtheFirstRowBeZeroed = True

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            shouldtheFirstColBeZeroed = True

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
        
    for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
    if shouldtheFirstRowBeZeroed:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    if shouldtheFirstColBeZeroed:
        for i in range(len(matrix)):
            matrix[i][0] = 0


s = [[1,2,3],
[4,0,6],
[7,8,9]]

setZeros(s)