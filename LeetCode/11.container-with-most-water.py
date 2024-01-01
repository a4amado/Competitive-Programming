#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
from math import floor


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        low = 0
        high = len(height) - 1
        while low < high:
            vertical_space = max(high, low) - min(high, low)
            hight = min(height[high], height[low])
            res = max(res, hight * vertical_space)
            if (height[high] > height[low]):
                low = low + 1
            else:
                high = high - 1
        return res

# @lc code=end
