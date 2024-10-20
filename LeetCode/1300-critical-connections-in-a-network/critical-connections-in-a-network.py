from typing import *
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Create adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize variables
        disc = [-1] * n  # Discovery time of each node
        low = [-1] * n   # Lowest discovery time of any node reachable
        parent = [-1] * n  # Parent of each node in DFS tree
        bridges = []
        self.time = 0
        
        def dfs(u):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            
            for v in graph[u]:
                if disc[v] == -1:  # If v is not visited
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                elif v != parent[u]:  # Back edge
                    low[u] = min(low[u], disc[v])
        
        # Call DFS for each unvisited node
        for i in range(n):
            if disc[i] == -1:
                dfs(i)
        
        return bridges
