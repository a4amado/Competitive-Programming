from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)

        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    new_distance = dp[j] + 1
                    if new_distance == dp[i]:
                        count[i] += count[j]
                    elif new_distance > dp[i]:
                        dp[i] = new_distance
                        count[i] = count[j]

        max_n = max(dp)
        idxs = [idx for idx, i in enumerate(dp) if i == max_n]

        return sum(count[idx] for idx in idxs)
