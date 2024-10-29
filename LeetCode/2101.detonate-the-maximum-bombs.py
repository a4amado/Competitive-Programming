from typing import List
import collections
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Build directed graph where each edge means bomb i can detonate bomb j
        adj = collections.defaultdict(list)
        n = len(bombs)
        
        # Check every pair of bombs
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    # Calculate if bomb i can reach bomb j
                    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if dist <= r1:
                        adj[i].append(j)
        
        def dfs(start: int) -> int:
            visited = set()
            stack = [start]
            
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    # Add all unvisited neighbors that can be detonated
                    for next_bomb in adj[curr]:
                        if next_bomb not in visited:
                            stack.append(next_bomb)
            return len(visited)
        
        # Try each bomb as the starting point and find max chain reaction
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, dfs(i))
        
        return max_bombs

# Test cases

solution = Solution()


bombs1 = [[1,2,3], [2,3,1], [3,4,2], [4,5,3], [5,6,4]]
print(solution.maximumDetonation(bombs1))