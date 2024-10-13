from sys import stdin
import sys
from typing import *

def cutRod(price: List[int], n: int):
    # price = {idx + 1: node for idx, node in enumerate(price)}
    def d(remainingRobLength: int, memo: Dict):
        if remainingRobLength == 0:return 0
        if remainingRobLength in memo: return memo[remainingRobLength]
        mm = float('-inf')
        for idx in range(1,n):
            if idx <= remainingRobLength:
                mm = max(mm, d(remainingRobLength - idx, memo) + price[idx - 1])
        memo[remainingRobLength] = mm
        return memo[remainingRobLength]
    memo = {}
    # result  = d(n, memo)
    # return result if result != float('-inf') else result
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        mm = float('-inf')
        for j in range(1, i + 1):
            mm = max(mm, price[j-1] + dp[i-j] )
        dp[i] = mm
    return dp[n]

print(
    cutRod(
        [3, 5, 6, 7, 10, 12], 6
    )
)

print(
    cutRod(
        [2,5,7,8,10], 5
    )
)


print(
    cutRod(
        [3, 5, 8, 9, 10, 17, 17, 20], 8
    )
)


