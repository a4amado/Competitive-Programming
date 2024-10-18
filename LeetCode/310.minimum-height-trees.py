#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
from typing import *

# @lc code=start
from typing import *

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:  # Special case where there's only one node
            return [0]
        
        # Initialize the adjacency list
        adjs = {i: set() for i in range(n)}
        
        # Build the adjacency list for the graph
        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)
        
        # Initialize the queue with all leaf nodes
        q = [i for i in range(n) if len(adjs[i]) == 1]
        
        # Trim the leaves level by level until 1 or 2 nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            nextLevel = []
            remaining_nodes -= len(q)  # Reduce the number of nodes
            
            # Process all the current leaves
            while q:
                leaf = q.pop()
                

                for neighbor in adjs[leaf]:
                    adjs[neighbor].remove(leaf)
                    if len(adjs[neighbor]) == 1:
                        nextLevel.append(neighbor)
            
            q = nextLevel
        
        
        return q

        
# @lc code=end



s = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print(
    s.findMinHeightTrees(n, edges)
)
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(
    s.findMinHeightTrees(n, edges)
)
n = 3
edges = [[0,1],[0,2]]

print(
    s.findMinHeightTrees(n, edges)
)