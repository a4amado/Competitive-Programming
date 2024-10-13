
from typing import List,Dict
from heapq import heappop, heappush

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        diffs = [[float('inf') for i in range(columns)] for _ in range(rows)]
        diffs[0][0] = float('-inf')
        q = []
        q.append([0, (0,0)])
        while q:
            diff, (row, col) = heappop(q)