from typing import List, Dict

def minSubsetSumDifference(arr: List[int]) -> int:
    total = sum(arr)
    target = total // 2

    def backtracking(idx: int, currentSum: int, memo: Dict):
        
        if idx >= len(arr):
            return abs((total - (target - currentSum)) - (target - currentSum))

        if (idx, currentSum) in memo:return memo[(idx, currentSum)]

        notTake = backtracking(idx + 1, currentSum ,memo)
        take = float('inf')
        if arr[idx] <= currentSum:
            take = backtracking(idx + 1, currentSum - arr[idx],memo)
        memo[(idx, currentSum)] = min(take, notTake)
        return memo[(idx, currentSum)]
    memo = {}
    # return backtracking(0, target, memo)
    dp = [
            [False for _ in range(target + 1)] for _ in range(len(arr) + 1)
        ]
    for i in range(len(dp)):
        dp[i][0] = 1
    for idx in range(1, len(dp)):
        for jdx in range(1, target + 1):
            dp[idx][jdx] = dp[idx - 1][jdx]
            
            if arr[idx - 1 ] <= jdx:
                dp[idx][jdx] = dp[idx][jdx] or dp[idx-1][jdx - arr[idx -1]]
    largest_achievable = 0
    for j in range(target, -1, -1):
        if dp[-1][j]:
            largest_achievable = j
            break
    return total - (largest_achievable * 2)

print(minSubsetSumDifference([8, 6, 5]))