#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

import heapq
from typing import *
from collections import defaultdict
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = {node: {} for node in range(1, n + 1)}
        for src, to, weight in times:
            adjs[src][to] = weight

        distances = {node: float('inf') for node in range(1, n + 1)}

        distances[k] = 0
        q = [(k, 0)]
        while q:
            node, distance =  heapq.heappop(q)
            for v, w in adjs[node].items():
                newWight = distance + w
                if newWight < distances[v]:
                    distances[v] = newWight
                    heapq.heappush(q, (v, newWight))
        m = max(distances.values())
        return m if m != float('inf') else -1
# @lc code=end

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
s = Solution()

print(
    s.networkDelayTime(times,n,k)
)

times = [[1,2,1]]
n = 2
k = 1

print(
    s.networkDelayTime(times,n,k)
)

times = [[1,2,1]]
n = 2
k = 2

print(
    s.networkDelayTime(times,n,k)
)
