#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
from typing import *

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {i+1:i+1 for i in range(len(edges) + 1)}
        ranks = {i+1:0 for i in range(len(edges) + 1)}
        
        # find the root of a set
        def find(x:int):
            # if node it's own parent return it
            # as it's the root 
            if x != parents[x]: 
                parents[x] = find(parents[x])
            return parents[x]
        
        def alreadyConnected(x: int, y: int):
            # find the root of both the 
            parent_x = find(x)
            parent_y = find(y)

            if parent_y == parent_x: return  True

            if ranks[parent_y] > ranks[parent_x]:
                parents[parent_x] = parent_y
            elif ranks[parent_y] < ranks[parent_x]:
                parents[parent_y] = parent_x
            else:
                parents[parent_y] = parent_x
                ranks[parent_x] += 1
            return False
        e = []
        for u,v in edges:
            if alreadyConnected(u, v): e = [u,v]
        return e