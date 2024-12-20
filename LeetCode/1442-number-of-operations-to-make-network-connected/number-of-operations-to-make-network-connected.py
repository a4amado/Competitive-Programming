from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1  # Not enough cables to connect all computers

        parents = list(range(n))

        def find(x: int) -> int:
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x: int, y: int):
            parents[find(x)] = find(y)

        for u, v in connections:
            union(u, v)
        
        count = 0
        for idx, val in enumerate(parents):
            if idx == val:
                count += 1
        return count -1
