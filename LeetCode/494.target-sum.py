from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # If the target is unreachable, return 0
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
        
        # Calculate the sum we need to achieve with positive numbers
        target_sum = (total + target) // 2
        
        # Memoization dictionary
        memo = {}
        
        def dfs(index: int, current_sum: int) -> int:
            # Base cases
            if index == len(nums):
                return 1 if current_sum == target_sum else 0
            
            # Check if this state has been computed before
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            
            # Recursive cases
            # Don't add the current number
            count = dfs(index + 1, current_sum)
            
            # Add the current number if possible
            if current_sum + nums[index] <= target_sum:
                count += dfs(index + 1, current_sum + nums[index])
            
            # Memoize the result
            memo[(index, current_sum)] = count
            return count
        
        return dfs(0, 0)

# Test the solution
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))  # Should print 5
print(s.findTargetSumWays([1], 1))  # Should print 1