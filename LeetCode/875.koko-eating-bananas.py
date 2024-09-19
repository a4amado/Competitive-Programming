#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def kWorks(k: int):
            hoursIsTakeToEatAllThePiles = 0
            for pile in piles:
                hoursIsTakeToEatAllThePiles += math.ceil(pile / k)
            return hoursIsTakeToEatAllThePiles <= h
        
        l,r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if kWorks(mid):
                r = mid
            else:
                l = mid + 1
        return l
# @lc code=end

