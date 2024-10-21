from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for i, (r, c) in enumerate(stones):
            rows[r].append(i)
            cols[c].append(i)

        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            r, c = stones[i]
            for j in rows[r]:
                uf.union(i, j)
                dfs(j)
            for j in cols[c]:
                uf.union(i, j)
                dfs(j)

        visited = set()
        for i in range(len(stones)):
            dfs(i)

        roots = set(uf.find(i) for i in range(len(stones)))
        return len(stones) - len(roots)


# Test cases
stones1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]

sol = Solution()
print(sol.removeStones(stones1))  # Expected output: 5
print(sol.removeStones(stones2))  # Expected output: 3