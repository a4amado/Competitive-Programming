from typing import List
from collections import defaultdict

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # nums.sort()
        n = len(nums)
        
        # `dp` will hold the length of the largest subset ending at each index
        dp = [1] * n
        # `prev` will help reconstruct the subset by storing the index of the previous element
        prev = [-1] * n
        
        max_len = 0
        max_index = -1
        
        # Fill dp array and track the indices for backtracking
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            # Track the maximum length and corresponding index
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]  # Reverse to get the subset in increasing order

# Test cases
nums = [1, 2, 3]
sol = Solution()
print(sol.largestDivisibleSubset(nums))

nums = [3, 17]
print(sol.largestDivisibleSubset(nums))

nums = [240, 4, 8, 10]
print(sol.largestDivisibleSubset(nums))
