from typing import List

class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        total = sum(arr)
        if (total - d) % 2 != 0 or total < d:
            return 0
        target = (total - d) // 2
        memo = {}
        MOD = 10**9 + 7

        # def count_subsets(idx: int, curr_sum: int) -> int:
        #     # Base case
        #     if idx == n:
        #         return 1 if curr_sum == 0 else 0

        #     # Check memoization
        #     if (idx, curr_sum) in memo:
        #         return memo[(idx, curr_sum)]

        #     # Recursive cases
        #     not_take = count_subsets(idx + 1, curr_sum)
        #     take = 0
        #     if arr[idx] <= curr_sum:
        #         take = count_subsets(idx + 1, curr_sum - arr[idx])

        #     # Store result in memo and return
        #     memo[(idx, curr_sum)] = (take + not_take) % MOD
        #     return memo[(idx, curr_sum)]

        # return count_subsets(0, target)
        dp = [[0 for i in range(target + 1)] for _ in range(len(arr) + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                # Recursive cases
                dp[i][j] = dp[i - 1][j]
                
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i][j] + dp[i - 1][j - arr[i - 1]]
        print(dp)

n = 4
d = 3
arr = [ 5, 2, 6, 4]
s = Solution()
print(
    s.countPartitions(n,d, arr)
)

n = 4
d = 0 
arr = [1, 1, 1, 1]

print(
    s.countPartitions(n,d, arr)
)
