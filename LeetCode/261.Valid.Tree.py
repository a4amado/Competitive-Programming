from typing import List
from collections import deque

# root 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check if the number of edges is correct for a tree
        if len(edges) != n - 1:
            return False

        # Create adjacency list
        adjs = [[] for _ in range(n)]
        for u, v in edges:
            # Check for self-loops
            if u == v:
                return False
            adjs[u].append(v)
            adjs[v].append(u)
        
        # BFS to check connectivity and cycles
        visited = set()

        q = deque([0])  # Start from node 0
        asdjs = [[] for _ in range(n)]
        while q:
            node = q.popleft()
            if node in visited:
                return False  # Cycle detected
            visited.add(node)
            
            for neighbor in adjs[node]:
                if neighbor not in visited:
                    asdjs[node].append(neighbor)
                    q.append(neighbor)

        # Check if all nodes are visited (graph is connected)
        return len(visited) == n

# Test the solution
s = Solution()
print(s.validTree(5, [[0,1],[1,3],[3,2],[1,4]]))  # Should print True
print(s.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # Should print False
print(s.validTree(1, [[0,0]]))  # Should print False