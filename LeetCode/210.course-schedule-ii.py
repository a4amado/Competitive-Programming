#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

from typing import List, Set
from collections import deque

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]
        
        adjs = [[] for _ in range(numCourses)]
        
        for [v, u] in prerequisites:
            if v == u:
                return []
            adjs[u].append(v)
        # use a self DFS
        # bc regulat algorithm that works in undirected graph
        # won't work here

        visited = set()
        selfVisited = set()
        
        # just detect a cycle
        def dfs(idx: int, visited:Set[int], selfVisited: Set[int]):

            if idx in selfVisited:
                return True
            visited.add(idx)
            selfVisited.add(idx)

            currAdjs = adjs[idx]

            for neigh in currAdjs:
                if dfs(neigh, visited, selfVisited):
                    return True

            selfVisited.remove(idx)
            
            return False
        for idx, _ in enumerate(adjs):
            if idx not in visited:
                if dfs(idx, visited, selfVisited):
                    return []
        
        def topological_sort(idx: int, memo: Set[int], l: List[int]):
     

            if idx in memo:return
            memo.add(idx)
                
            for i in adjs[idx]:
                topological_sort(i, memo, l)
            
            l.append(idx)
            return l
        
        memo = set()
        l = []
        for i in range(len(adjs)):
            if i not in memo:
                topological_sort(i, memo, l)

        return l[::-1]
              
            

s = Solution()
print(s.findOrder(2, [[0,1]]))
print(s.findOrder(3, [[0,1],[0,2],[1,2]]))




            

        
        
# @lc code=end

# print(s.findOrder(2, [[1,0]]))
# print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
