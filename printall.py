class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
       
        # we would set the first two numbers of the array to 1 bc we will need them later
        dp[0] = dp[1] = 1

        # loop till reach n 
        # skip the first 2
        for i in range(2, n +1):
            # calud the all the possible tree that it's length does not ecxeed i
            # try all elements from 1 til i as a root for the tree
            l = 0
            r = i - 1
            while r != -1:
                dp[i] += dp[l] * dp[r]
                l += 1
                r -= 1

        return dp[n]