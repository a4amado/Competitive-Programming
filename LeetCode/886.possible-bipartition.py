#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
from typing import *
# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjs = {idx: set() for idx in range(1, n+1)}
        for u,v in dislikes:
            adjs[u].add(v)
            adjs[v].add(u)

        groups = {idx: {} for idx in range(1, n+1)}

        def d(idx: int, group: int):
            if groups[idx]:
                return groups[idx] == group

            groups[idx] == group
            
            for i in adjs[idx]:
                if not d(i, 1 if group == 2 else 2):
                    return  False
            return True
        for i in range(1, n + 1):
            if not groups[i] and not d(i, 1):
                return False
        return True
        
# @lc code=end

