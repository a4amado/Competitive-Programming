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
        max_sequence = 0
        
        for num in num_set:
            # Only start counting if this is the start of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                max_sequence = max(max_sequence, current_streak)
        
        return max_sequence