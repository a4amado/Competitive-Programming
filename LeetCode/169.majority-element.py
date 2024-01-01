#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        return int(max(d, key=lambda k: d[k]))
# @lc code=end
