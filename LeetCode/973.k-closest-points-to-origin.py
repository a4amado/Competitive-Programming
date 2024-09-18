#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#


from typing import List
import math
from heapq import heapify, heappush, heappop 

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(x:int, y:int,x2:int, y2: int):
            return math.sqrt((x-x2)**2 + (y-y2)**2)
        
        distances: List[List[int]] = []

        for point in points:
            dist = distance(point[0], point[1], 0, 0)
            heappush(distances, [dist, point[0], point[1]])
        
        return [[x[1], x[2]] for x in [heappop(distances) for x in range(0, k)] ]


s = Solution()
print(s.kClosest([[3,3],[5,-1],[-2,4]], 2))
# @lc code=end

