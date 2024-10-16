#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#
from typing import *
from collections import deque

# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if not manager:return 0
        adjs = [[] for i in range(n)]
        for to, respondsTo in enumerate(manager):
            if respondsTo == -1:continue
            adjs[respondsTo].append([to, informTime[respondsTo]])
        # find heaviest path stating from headId

        q = deque([(headID, 0)])
        maxWeight = 0

        while q:
            newQ = deque([])
            while q:
                node, weight = q.popleft()
                for nei, NeiWeight in adjs[node]:
                    newWeight = NeiWeight + weight
                    maxWeight = max(newWeight, maxWeight)
                    q.append((nei, newWeight))
            q = newQ

        return maxWeight
