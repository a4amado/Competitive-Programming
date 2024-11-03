from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # The target we want after considering positive numbers
        sum_wanted = total - (total - target)  # This simplifies to just target
        memo = {}
        
        def recur(idx: int, sum_til_now: int) -> int:
            key = (idx, sum_til_now)
            if key in memo:
                return memo[key]
                
            if idx >= len(nums):
                if sum_til_now == sum_wanted:
                    return 1
                return 0

            # Add this number
            take = recur(idx + 1, sum_til_now + nums[idx])
            # Subtract this number
            noTake = recur(idx + 1, sum_til_now - nums[idx])
            
            memo[key] = take + noTake
            return memo[key]
            
        return recur(0, 0)

# Test the solution
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))  # Should print 5
print(s.findTargetSumWays([1], 1))  # Should print 1