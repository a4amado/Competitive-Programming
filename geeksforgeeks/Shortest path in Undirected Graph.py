#User function Template for python3
from typing import *
from collections import deque
class Solution:
    def shortestPath(self, edges:List[List[int]], n:int, m:int, src:int):

        adjs = [[] for _ in range(n)]
        
        for adj in edges:
            adjs[adj[0]].append(adj[1])
            adjs[adj[1]].append(adj[0])
        
        distances = [-1] * n

        q = deque([(0, src)])
        visitedSet = set()

        while q:
            (level, idx) = q.popleft()
            if idx in visitedSet: continue
            visitedSet.add(idx)
            distances[idx] = level

            for adj in adjs[idx]:
                if adj in visitedSet: continue
                if adj == idx: continue
                q.append((level + 1, adj))

        # DFS
        # def dfs(idx:int, sumTilNow: int, parent: int):
        #     if distances[idx] != -1:
        #         if sumTilNow > distances[idx]:return
            
            

        #     distances[idx] = sumTilNow
            
        #     for nei in adjs[idx]:
        #         if nei == idx:continue
        #         if nei == parent:continue
        #         dfs(nei, sumTilNow + 1, idx)
        # dfs(src,0, -1)
        
        return distances



# 0 1 2 1 2 3 3 4 4



n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0

s = Solution()
print(
    s.shortestPath(edges, n, m, src)
)

n = 4
m = 2
edges=[[1,3],[3,0]] 
src=3

s = Solution()
print(
    s.shortestPath(edges, n, m, src)
)