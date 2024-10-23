from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # If the matrix is 1x1, return 0
        if rows == 1 and cols == 1:
            return 0
            
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Initialize efforts matrix with infinity
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Priority queue to store (effort, row, col)
        pq = [(0, 0, 0)]  # (effort, row, col)
        
        while pq:
            curr_effort, row, col = heapq.heappop(pq)
            
            # If we reached the target, return the effort
            if row == rows - 1 and col == cols - 1:
                return curr_effort
            
            # If we've found a better path to this cell, skip this one
            if curr_effort > efforts[row][col]:
                continue
            
            # Check all adjacent cells
            for dy, dx in directions:
                new_row, new_col = row + dy, col + dx
                
                # Skip if out of bounds
                if not (0 <= new_row < rows and 0 <= new_col < cols):
                    continue
                
                new_effort = max(curr_effort, abs(heights[row][col] - heights[new_row][new_col]))


                # If we found a better path to the adjacent cell
                if new_effort < efforts[new_row][new_col]:
                    efforts[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))
        
        return efforts[-1][-1]

# Test cases
sol = Solution()
# Test case 1: Example from problem
print(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))  # Expected: 2

# Test case 2: Single cell
print(sol.minimumEffortPath([[3]]))  # Expected: 0

# Test case 3: Single row
print(sol.minimumEffortPath([[1,10,6,7,9,10,4,9]]))  # Expected: 3