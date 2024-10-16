#
# @lc app=leetcode id=1334 lang=python3
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#
from typing import *
from heapq import *
# @lc code=start
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf') for i in range(n)]for i in range(n)]
        for u, v, w in edges:
            matrix[u][v] = w
            matrix[v][u] = w
        
        for i in range(n):
            matrix[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])
      
        ss = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if j == i:continue
                if matrix[i][j]  <= distanceThreshold:
                    ss[i] += 1
        
        minValToLookFor = min(ss)
        allMinimums = [idx for idx, val in enumerate(ss) if val == minValToLookFor]

        return allMinimums[-1]
        
        
# @lc code=end

n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4

s = Solution()
print(
    s.findTheCity(n, edges, distanceThreshold)
)

n= 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

print(
    s.findTheCity(n, edges, distanceThreshold)
)
