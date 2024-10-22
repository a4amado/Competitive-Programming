#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        num_set = set(nums)
        visited = set()
        max_sequence = 0
        
        for num in nums:
            # Only start counting if this is the start of a sequence
            # (i.e., num-1 is not in the set)
            if num not in visited:
                visited.add(num)
                currunt_streak = 1

                going_downward = num - 1
                going_forward = num + 1

                while going_downward in num_set:
                    visited.add(going_downward)
                    currunt_streak += 1
                    going_downward -= 1

                while going_forward in num_set:
                    visited.add(going_forward)
                    currunt_streak += 1
                    going_forward += 1
                    

                max_sequence = max(max_sequence, currunt_streak)
                
        return max_sequence