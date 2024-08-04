
#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List

# @lc code=start
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0
        for i in unique:
            if (i - 1) not in  unique:
                length = 0
                while i + length in unique:
                    length = length + 1
                longest = max(length, longest)

        return longest


# @lc code=end
