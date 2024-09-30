from typing import *
MOD = 10**9 + 7

def mazeObstacles(n: int, m:int, mat: List[List[int]]):
    rows, cols = len(mat), len(mat[0])
    dp = [
        [0 for x in range(cols)] for _ in range(rows)
    ]

    for cdx, col in enumerate(mat[0]):
        if col == -1:break
        dp[0][cdx] = 1

    for rdx in range(len(mat)):
        if mat[rdx][0] == -1:break
        dp[rdx][0] = 1

    for rdx in range(1, rows):
        for cdx in range(1, cols):
            if mat[rdx][cdx] == -1:
                continue
            else:
                dp[rdx][cdx] = (max(0,dp[rdx - 1][cdx]) + max(0, dp[rdx][cdx - 1])) % MOD


    return dp[-1][-1]

