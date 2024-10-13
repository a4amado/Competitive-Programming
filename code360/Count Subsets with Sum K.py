from typing import List

def findWays(arr: List[int], k: int) -> int:

    memo = {}

    def power(idx: int, currSum: int):
        if idx == len(arr): 
            if currSum == k: return 1
            return 0
        if (idx, currSum) in memo: return memo[(idx, currSum)]
        take = 0
        if arr[idx] <= k - currSum:
            take += power(idx + 1, currSum + arr[idx])
        take += power(idx + 1, currSum)
        
        memo[(idx, currSum)] = take
        return memo[(idx, currSum)]
    return power(0, 0)


    # dp = [[0 for _ in range(k + 1)] for _ in range(len(arr) + 1)]
    # MOD = 10**9 + 7

    # # Initialize base case
    # for i in range(len(dp)):
    #     dp[i][0] = 1

    # # Iterate over elements in decreasing order
    # for i in range(1, len(arr) + 1):
    #     for j in range(k + 1):
    #         # Exclude the current element
    #         dp[i][j] = dp[i - 1][j]

    #         # Include the current element if it's not greater than j
    #         if arr[i - 1] <= j:
    #             dp[i][j] += dp[i - 1][j - arr[i - 1]]
    #         dp[i][j] %= 10 ** 9 + 7
            

    
    # return dp[-1][k]

print(findWays([0, 1, 0], 0))  # This should now return 2

# from typing import List

# def findWays(arr: List[int], k: int) -> int:
#     dp = [[0 for _ in range(k + 1)] for _ in range(len(arr) + 1)]
#     MOD = 10**9 + 7

#     # Initialize base case
#     for i in range(len(dp)):
#         dp[i][0] = 1

#     # Iterate over elements in increasing order
#     for i in range(1, len(arr) + 1):
#         for j in range(k + 1):
#             # Exclude the current element
#             dp[i][j] = dp[i - 1][j]
#             # Include the current element if it's not greater than j
#             if arr[i - 1] <= j:
#                 dp[i][j] += dp[i - 1][j - arr[i - 1]]
#             dp[i][j] %= MOD

#     return dp[-1][k]

print(findWays([0, 0, 1], 1))  # This should now return 2
 
# print(findWays([1,4,4,5], 5))
# print(findWays([1,1,1], 2))



# print(findWays([0,1,3], 4))
# print(findWays([2,34,5], 40))

