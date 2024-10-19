from typing import List
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(i, j):
            visited.add((i, j))
            for ni, nj in stones:
                if (ni, nj) not in visited and (ni == i or nj == j):
                    dfs(ni, nj)

        visited = set()
        islands = 0
        for i, j in stones:
            if (i, j) not in visited:
                dfs(i, j)
                islands += 1

        return len(stones) - islands