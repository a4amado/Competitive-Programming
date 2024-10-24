#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List


from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        l = list(count)
        l.sort(key=lambda x:x[1], reverse=True)
        return l[0][0]
# @lc code=end
