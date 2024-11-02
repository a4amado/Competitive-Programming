from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)




# Test the solution
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))  # Should print 5
print(s.findTargetSumWays([1], 1))  # Should print 1