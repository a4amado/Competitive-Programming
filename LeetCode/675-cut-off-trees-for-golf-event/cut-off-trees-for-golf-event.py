from typing import List
from heapq import heappush, heappop

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or forest[0][0] == 0:
            return -1
            
        # Get sorted trees
        trees = []
        for i, row in enumerate(forest):
            for j, height in enumerate(row):
                if height > 1:
                    trees.append((height, i, j))
        trees.sort()
        
        def manhattan(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)
        
        def astar(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
                
            R, C = len(forest), len(forest[0])
            heap = [(manhattan(sr, sc, tr, tc), 0, sr, sc)]
            seen = {(sr, sc)}
            
            while heap:
                f, steps, r, c = heappop(heap)
                if r == tr and c == tc:
                    return steps
                    
                for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if (0 <= nr < R and 0 <= nc < C and 
                        (nr, nc) not in seen and forest[nr][nc] > 0):
                        seen.add((nr, nc))
                        h = manhattan(nr, nc, tr, tc)
                        heappush(heap, (steps + 1 + h, steps + 1, nr, nc))
            return -1
            
        ans = 0
        sr = sc = 0
        for _, tr, tc in trees:
            d = astar(sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans