from typing import List
from collections import deque

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 2  # Total number of nodes
        adjs = [set() for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(1, n) if degree[i] == 1])
        
        while len(leaves) > 1:
            newLeaves = deque()
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                for nei in adjs[leaf]:
                    if degree[nei] == 0:
                        continue
                    adjs[nei].remove(leaf)
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        newLeaves.append(nei)
                degree[leaf] = 0
            
            leaves = newLeaves

        return leaves[0]  # The last remaining node is the center
