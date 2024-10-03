# adjs = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 

from typing import *
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adjs: List[List[int]]) -> bool:
        

        def dfs(idx:int, parent:int, visited: Dict):
            if idx == parent: return False
            if idx != parent and idx in visited: return True

            visited[idx] = True
            for  nei in adjs[idx]:
                if nei in visited and parent == -1 or nei == parent: continue
                if dfs(nei, idx, visited): return True
            return False
        
        visited = {}
        for i in range(len(adjs)):
            if i in visited: continue
            if dfs(i, -1, visited): return True
        return False

        # def bfs(idx: int, visited: Dict):
        #     q = deque([(idx, -1)])
            
            
        #     while q:
        #         (v, parent) = q.popleft()
                
        #         curr = adjs[v]
        #         for adj in curr:
        #             if adj != parent:
        #                 if adj in visited:return True
        #                 q.append((adj, v))
        #         visited[v] = True
        #     return False
        # visited = {}
        # for idx in range(len(adjs)):
        #     if idx not in visited:
        #         if bfs(idx, visited): return True
        # return False

s= Solution()
# print(s.isCycle(0, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] ))
print(s.isCycle(0, [[], [2], [1, 3], [2]]))
