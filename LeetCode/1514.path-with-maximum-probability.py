#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#
from typing import *
import heapq

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjs = {idx: [] for idx in range(n)}

        for idx, (u,v) in enumerate(edges):
            w = succProb[idx] 
            adjs[u].append((v, w))
            adjs[v].append((u, w))
        
        q = []
        
        heapq.heappush(q, (-1, start_node))
        visited = set()
        maxPathProp = float('-inf')

        while q:
            weight, node  = heapq.heappop(q)
            weight = -weight

            if node in visited: continue

            visited.add(node)
            if node == end_node:
                maxPathProp = max(weight, maxPathProp)
                continue
            
            for nei, neiWeight in adjs[node]:
                if nei in visited:continue
                newWeight = neiWeight * weight
                heapq.heappush(q, (-newWeight, nei))
        return maxPathProp if maxPathProp != float('-inf') else float(0)
    
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
a = Solution()
print(
    a.maxProbability(

n,
edges,
succProb,
start,
end,
)
)








# @
# lc code=end

