from sys import *
from collections import *
from math import *

def minInsertion(s: str):
    
    str1 = s
    str2 = "".join(list(s)[::-1])
    # dp = [
    #     [
    #         0 for _ in range(len(s) + 1)
    #     ] for _ in range(len(s) + 1)
    # ]
    curr = [0 for _ in range(len(s) + 1)] 
    prev = [0 for _ in range(len(s) + 1)] 

    currMax = float('-inf')
    for idx in range(1, len(s) + 1):
        for jdx in range(1, len(s) + 1):
            if str1[idx-1] == str2[jdx-1]:
                curr[jdx] = prev[jdx-1] + 1
            else:
                curr[jdx] = max(prev[jdx], curr[jdx -1])
            currMax = max(currMax, curr[jdx])
        curr, prev = prev, curr
    return len(s) - prev[-1]


print(minInsertion("abca"))
