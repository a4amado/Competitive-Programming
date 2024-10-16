class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # Find the root of the set containing node u, with path compression
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    # Union the sets containing u and v, with union by rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank to keep the tree flat
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal(n, edges):
    # Initialize the union-find data structure for n nodes
    uf = UnionFind(n)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    mst = []
    mst_cost = 0

    # Iterate through the sorted edges
    for u, v, weight in edges:
        # Check if adding this edge forms a cycle
        if uf.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost


# Example usage:
# n is the number of nodes, edges is a list of tuples (u, v, weight)
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, mst_cost = kruskal(n, edges)

print("Edges in the Minimum Spanning Tree:", mst)
print("Total cost of the Minimum Spanning Tree:", mst_cost)
