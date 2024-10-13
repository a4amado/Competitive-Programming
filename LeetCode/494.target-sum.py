from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        memo = {}


        def power(idx: int, currSum: int):
            if idx == len(nums):
                if currSum == target: return 1
                return 0

            if (idx, currSum) in memo: return memo[(idx, currSum)]

            ss = 0
            if nums[idx] <= target - currSum:
                ss += power(idx+1, currSum + nums[idx])
            
            ss += power(idx+1, currSum )
            memo[(idx, currSum)] = ss
            return memo[(idx, currSum)]
            
        
        return power(0, 0)



# Test the solution
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))  # Should print 5
print(s.findTargetSumWays([1], 1))  # Should print 1