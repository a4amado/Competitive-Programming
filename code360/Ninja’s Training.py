from typing import *

# [
#   [1,2,5],
#   [3,1,1],
#   [3,3,3]
# ]
  
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # memo = {}

    # def dfs(idx: int, day: int):
    #     # idx is the choise of the day before, skip it
    #     if day >= len(points):return 0
    #     if (idx, day) in memo:return memo[(idx, day)]
    #     maxMerisOftheDay = float('-inf')
    #     for cdx, val in enumerate(points[day]):
    #         if idx == cdx:continue
    #         maxMerisOftheDay = max(maxMerisOftheDay, val + dfs(cdx, day+1))
    #     memo[(idx, day)] = maxMerisOftheDay
    #     return maxMerisOftheDay

    dp = [[float('-inf') for _ in range(3)] for _ in range(len(points))]
    
    dp[0] = points[0][:]
    for i in range(1, len(dp)):
        dp[i][0] = points[i][0] + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = points[i][1] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = points[i][2] + max(dp[i-1][0], dp[i-1][1])
    
    return max(dp[-1])
print(ninjaTraining(0, [
    [10,40,70],
    [20,50,80],
    [30,60,90],
    ]
))
