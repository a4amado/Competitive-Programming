#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
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
            for j in range(1, i + 1):
                # number of element left of the root if the number of the 
                left = dp[j - 1]
                right = dp[i - j]
                dp[i] += left * right

        return dp[n]

                
        

s = Solution()
s.numTrees(7)

# @lc code=end

