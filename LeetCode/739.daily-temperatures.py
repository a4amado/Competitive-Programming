#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = []
        diff = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            if l:
                while l:
                    (prevIdx, prevTemp) = l[-1]
                    if prevTemp < temp:
                        diff[prevIdx]= abs(idx - prevIdx)
                        l.pop()
                    else:break
            l.append((idx, temp))
        return diff
            
# @lc code=end

s = Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])
