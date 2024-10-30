#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

from typing import List

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(set(nums1) & set(nums2)))
# @lc code=end

