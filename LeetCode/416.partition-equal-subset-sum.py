from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        memo = {}
        



        def backtracking(i: int, currSum: int):
            if currSum == target:
                return True
            
            if (i, currSum) in memo:
                return False
            if currSum > target:
                return False
            if i >= len(nums):
                return False

            
            if backtracking(i+1, currSum + nums[i]):
                return True
            if backtracking(i+1, currSum):
                return True
            memo[(i, currSum)] = False

            return False

        # return backtracking(0, 0)


s = Solution()
s.canPartition([1,5,11,5])