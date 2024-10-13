from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def dijkstra(self, V: int, adj: List[List[int]], S: int, target: int) -> List[int]:
        
        
        distances = [[] for i in range(V)]
        distances[S] = [-1 ,S, float('-inf')]


        q = []
        for node in adj[S]:
            currNode = node[0]
            weight = node[1]
            distances[currNode] = [S, currNode, weight]
            q.append(distances[currNode])

        while q:
            comming, node, weightTilNow = heappop(q)
            
            for nei, weight in adj[node]:
                if nei == node: continue
                if distances[nei]:
                    weightOfTheNei = distances[nei][-1]
                    ToGoWeight = weightTilNow + weight
                    if ToGoWeight > weightOfTheNei: continue

                distances[nei] = [
                    node,
                    nei,
                    weightTilNow + weight
                ]
                q.append(distances[nei])
        path = []
        pp = distances[target]
        while True:
            if path and path[-1] == S:break
            path.append(pp[1])
            pp = distances[pp[0]]
        path.reverse()
        return path


V = 3
E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
S = 2
target = 0
s = Solution()
print(
    s.dijkstra(V, adj, S, target)
)
