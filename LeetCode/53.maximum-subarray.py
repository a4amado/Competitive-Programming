
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        curr_max = 0
        final_max = nums[0]
        for num in nums:
            if curr_max < 0:
                curr_max = 0
            curr_max += num
            final_max = max(final_max, num)

        return final_max


s = Solution()
print(s.maxSubArray([-2,-1]))