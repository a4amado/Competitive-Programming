#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

from typing import *
from collections import defaultdict


# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = defaultdict(int)
        for city1, city2 in paths:
            cities[city1] = 0
            cities[city2] = 0
        for city1, _ in paths:
            cities[city1] += 1
        
        for key, num in cities.items():
            if num == 0: return key
        
        
# @lc code=end

