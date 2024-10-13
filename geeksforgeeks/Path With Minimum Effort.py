from typing import List
from heapq import heappop, heappush

class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        rows = len(heights)
        columns = len(heights[0])
        diffs = [[float('inf') for _ in range(columns)] for _ in range(rows)]
        diffs[0][0] = 0
        q = [(0, 0, 0)]  # (effort, row, col)
        
        while q:
            effort, row, col = heappop(q)
            
            if row == rows - 1 and col == columns - 1:
                return effort
            
            for y, x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                newRow, newCol = row + y, col + x
                
                if 0 <= newRow < rows and 0 <= newCol < columns:
                    new_effort = max(effort, abs(heights[row][col] - heights[newRow][newCol]))
                    if diffs[newRow][newCol] == float('inf'):
                        diffs[newRow][newCol] = new_effort
                        heappush(q, (new_effort, newRow, newCol))
                    else:
                        if diffs[newRow][newCol]  > new_effort:
                            diffs[newRow][newCol] = new_effort
                            heappush(q, (new_effort, newRow, newCol))
        
        return -1  # If no path is found

# Test the solution
ss = [
    # 1    0
    [1, 2, 2],
 [3, 8, 2],
 [5, 3, 5]
]

s = Solution()
print(s.MinimumEffort(3, 3, ss))
