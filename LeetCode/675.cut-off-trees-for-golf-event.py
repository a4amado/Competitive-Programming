from typing import List
from heapq import heappush, heappop

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Check if the forest is valid or if the starting point is blocked (0 means no tree)
        if not forest or forest[0][0] == 0:
            return -1
            
        # Collect all trees with height > 1 into a list and sort by height (ascending order)
        trees = []
        for i, row in enumerate(forest):
            for j, height in enumerate(row):
                if height > 1:
                    trees.append((height, i, j))
        trees.sort()  # Trees sorted by height, so we cut the shortest trees first
        
        # Define a Manhattan distance heuristic function for A*
        def manhattan(r1, c1, r2, c2):
            # Manhattan distance is the sum of absolute differences in rows and columns
            return abs(r1 - r2) + abs(c1 - c2)
        
        # A* search function to find the shortest path between (sr, sc) and (tr, tc)
        def astar(sr, sc, tr, tc):
            # If the starting point is the target point, no movement is required
            if sr == tr and sc == tc:
                return 0
                
            # Initialize the grid size
            R, C = len(forest), len(forest[0])
            
            # Min-heap initialized with the first node (heuristic value, cost so far, row, column)
            heap = [(manhattan(sr, sc, tr, tc), 0, sr, sc)]
            
            # Set to track the nodes we've already visited
            seen = {(sr, sc)}
            
            # Process nodes from the priority queue (min-heap)
            while heap:
                # Pop the node with the smallest `f(n)` = `g(n) + h(n)`
                f, steps, r, c = heappop(heap)
                
                # If we've reached the target, return the number of steps (g(n))
                if r == tr and c == tc:
                    return steps
                    
                # Explore all neighboring cells (up, down, left, right)
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    # Check if the neighbor is within bounds, hasn't been seen, and is not blocked
                    if (0 <= nr < R and 0 <= nc < C and 
                        (nr, nc) not in seen and forest[nr][nc] > 0):
                        
                        # Mark the neighbor as seen
                        seen.add((nr, nc))
                        
                        # Compute the Manhattan distance from the neighbor to the target (h(n))
                        h = manhattan(nr, nc, tr, tc)
                        
                        # Push the neighbor onto the heap with its new cost and heuristic
                        # The tuple is (f(n), g(n), nr, nc) where:
                        # - f(n) = steps + 1 (g(n)) + h (heuristic)
                        # - steps + 1 is the new g(n) (cost so far)
                        heappush(heap, (steps + 1 + h, steps + 1, nr, nc))
                        
            # If no valid path to the target, return -1
            return -1
            
        # Initialize the total cost (number of steps) to 0
        ans = 0
        
        # Start from the top-left corner (0, 0)
        sr = sc = 0
        
        # For each tree, find the shortest path to it using A* and add the steps to the total
        for _, tr, tc in trees:
            d = astar(sr, sc, tr, tc)  # Perform A* from current position to the tree's position
            if d < 0: return -1  # If any tree is unreachable, return -1
            ans += d  # Add the number of steps to the total distance
            sr, sc = tr, tc  # Move to the position of the last tree
            
        # Return the total steps needed to cut all trees in order
        return ans
