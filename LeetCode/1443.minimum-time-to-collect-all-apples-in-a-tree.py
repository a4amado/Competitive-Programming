#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def find_path(self, path_edges: set, adjs: dict, start: int, target: int = 0) -> None:
        # If start is already target, nothing to do
        if start == target:
            return
            
        # Track parents and visited nodes
        n = len(adjs)
        parent = [-1] * n
        visited = [False] * n
        
        # BFS starting from target (node 0)
        q = deque([target])
        visited[target] = True
        found = False
        
        while q and not found:
            curr = q.popleft()
            
            for nei in adjs[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = curr
                    if nei == start:
                        found = True
                        break
                    q.append(nei)
        
        # If we found a path, add its edges to the set
        if visited[start]:
            curr = start
            while curr != target:
                next_node = parent[curr]
                # Add edge in ascending order
                path_edges.add((min(curr, next_node), max(curr, next_node)))
                curr = next_node
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjs = {idx: set() for idx in range(n)}

        for u,v in edges:
            adjs[u].add(v)
            adjs[v].add(u)

        visted = set()
        for i in range(n):
            if hasApple[i]:
                self.find_path(visted, adjs, i, 0)
        return len(visted) * 2

# @lc code=end

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
sol = Solution()
print(sol.minTime(n, edges, hasApple))
