
from typing import List

from collections import deque

class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        if not edges:return [-1]
        # code here
        adj  = [[] for i in range(n)]
        for ver in edges:
            src =  ver[0] -1
            to =  ver[1] -1
            weight =  ver[2]
            adj[src].append([to , weight])
            adj[to].append([src , weight])

        
        distances = [[] for i in range(n)]
        distances[0] = [0, float('-inf')]


        q = deque([])
        for node in adj[0]:
            currNode = node[0]
            weight = node[1]
            distances[currNode] = [currNode, weight]
            q.append(distances[currNode])

        while q:
            node, weightTilNow = q.popleft()
            
            for nei, weight in adj[node]:
                if nei == node: continue
                if distances[nei]:
                    weightOfTheNei = distances[nei][-1]
                    ToGoWeight = weightTilNow + weight
                    if ToGoWeight > weightOfTheNei: continue

                distances[nei] = [nei,weightTilNow + weight]
                q.append(distances[nei])
        if distances[-1][-1] == float('inf'): return [-1]
        return [distances[-1][-1]]




n = 5
m= 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]

s = Solution()
print(
    s.shortestPath(n,m,edges)
)


n = 2
m= 1
edges = [[1, 2, 2]]

print(
    s.shortestPath(n,m,edges)
)

n = 2
m= 1
edges = []

print(
    s.shortestPath(n,m,edges)
)