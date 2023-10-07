from sys import stdout
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            for i, num_1 in enumerate(nums):
                if (idx == i):
                    continue
                if num + num_1 == target:
                    
                    return  sorted([idx, i])
        return []

# @lc code=end

