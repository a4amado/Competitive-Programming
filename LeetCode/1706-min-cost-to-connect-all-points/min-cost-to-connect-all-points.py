class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            # Path compression: make each node point directly to root
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, rank, x, y):
            # Union by rank: attach smaller rank tree under root of higher rank tree
            px, py = find(parent, x), find(parent, y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True
        
        n = len(points)
        # Generate all edges with their weights
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate Manhattan distance
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        
        # Sort edges by weight (distance)
        edges.sort()
        
        # Initialize Union-Find data structures
        parent = list(range(n))
        rank = [0] * n
        
        # Kruskal's algorithm
        total_cost = 0
        edges_used = 0
        
        for weight, u, v in edges:
            if union(parent, rank, u, v):
                total_cost += weight
                edges_used += 1
                # Early termination: MST will have n-1 edges
                if edges_used == n - 1:
                    break
        
        return total_cost