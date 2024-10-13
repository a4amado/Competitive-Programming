from typing import List, Dict
import heapq


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = [[] for _ in range(n)]
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        distances = [[float('inf'), 0] for i in range(n)]
        distances[0] = [0, 1]
        q = [[0,0]]

        while q:
            weight, node  = heapq.heappop(q)
            for u, w in graph[node]:
                newWeight = weight + w
                if newWeight < distances[u][0]:
                    distances[u] = [newWeight, distances[node][1]]
                    heapq.heappush(q, [newWeight, u])
                elif newWeight == distances[u][0]:
                    distances[u][1] = (distances[u][1] + distances[node][1]) % MOD
          
        return distances[-1][-1]
# Test the solution
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
s = Solution()
print(s.countPaths(n, roads))