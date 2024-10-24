class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1  # Base cases

        # Calculate dp[i] for each i from 2 to n
        for i in range(2, n + 1):
            l = 0
            r = i - 1
            while l <= r:  # Loop until r becomes -1
                if r == l:
                    dp[i] += (dp[l] * dp[r])
                else:
                    dp[i] += (dp[l] * dp[r]) * 2
                l += 1
                r -= 1

        return dp[n]