#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

from typing import List

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        if len(nums) == 0:
            return False

        maxReach = 0  # This will store the farthest index we can reach

        for i in range(len(nums)):
            # that mean you keept looping and mazimize the maxReact but even with that you didn't accumilate enough max to reach it
            if i > maxReach:  # If the current index is beyond our maxReach, we can't reach it
                return False
            
            maxReach = max(maxReach, i + nums[i])  # Update maxReach at each step
            if maxReach >= len(nums) - 1:  # If we can reach or exceed the last index, return True
                return True

        return False



        # if len(nums) == 1 :
        #     return True
        # if len(nums) == 0 :
        #     return False

        
        # dp = [0] * len(nums)
        # dp[0] = 1
        # for idx, val in enumerate(nums[:len(nums) - 1]):
        #     if dp[idx] == 0:
        #         continue
        #     for j in range(idx+1, min(idx+val+1, len(nums))):
        #         dp[j] += 1
        #         if j == len(nums) - 1:
        #             return True
        # return False

s = Solution()
print(s.canJump([0,2,3]))

# @lc code=end

