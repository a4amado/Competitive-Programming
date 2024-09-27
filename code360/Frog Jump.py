# https://www.naukri.com/code360/problems/frog-jump_3621012

from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(heights: List[int], steps: int) -> int:
    n = len(heights)
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(max(0, i - steps), i):
            dp[i] = min(dp[i], dp[j] + abs(heights[i] - heights[j]))
    
    return dp[-1]

# Example usage
print(frogJump([10, 20, 30, 10, 50, 90, 5], 3))

print(frogJump(4, [10,20,30,10,50,90,5],3))
# print(frogJump(3, [10, 50, 10],3))
