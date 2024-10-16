from os import *
from sys import *
from collections import *
from math import *

def getLengthOfLCS(str1, str2):
    dp = [[0 for i in range(len(str1) +1) ] for i in range(len(str2) +1) ]

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if str1[j-1] == str2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]