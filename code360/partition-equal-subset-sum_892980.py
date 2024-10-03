
# def backtracking(idx: int, curr: int, memo: Dict):
#     if curr == 0:
#         if idx >= len(arr):return False
#         return True
#     if idx >= len(arr): return False
#     if (idx, curr) in memo: return memo[(idx, curr)]

#     take = backtracking(idx+1, curr - arr[idx], memo)
#     notTake = backtracking(idx+1, curr,memo)
#     memo[(idx, curr)] = take or notTake
#     return memo[(idx, curr)]
# memo = {}
from typing import List

def canPartition(nums: List[int], n) -> bool:
    """
    Determines whether a given array of integers can be partitioned into two
    subsets with equal sums.

    Args:
        nums: The array of integers to be partitioned.

    Returns:
        True if the array can be partitioned, False otherwise.
    """

    total_sum = sum(nums)

    # If the total sum is odd, it cannot be partitioned equally.
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2

    # Create a dynamic programming table with dimensions (n+1) x (target_sum+1).
    # Initialize all values to False.
    dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

    # Base case: An empty subset (i=0) can always achieve a sum of 0.
    for i in range(len(nums) + 1):
        dp[i][0] = True

    # Iterate through the array elements (i) and the target sums (j).
    for i in range(1, len(nums) + 1):
        for j in range(1, target_sum + 1):
            # If the current element (nums[i-1]) is less than or equal to the
            # target sum (j), consider two possibilities:
            # 1. Include the current element: dp[i][j] = dp[i-1][j-nums[i-1]]
            # 2. Exclude the current element: dp[i][j] = dp[i-1][j]
            dp[i][j] = dp[i-1][j] or (nums[i-1] <= j and dp[i-1][j-nums[i-1]])

    # The final result is stored in dp[n][target_sum].
    return dp[len(nums)][target_sum]

