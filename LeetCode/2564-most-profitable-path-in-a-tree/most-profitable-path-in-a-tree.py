from typing import *
from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adjs = {i: set() for i in range(n)}
        for u, v in edges:
            adjs[u].add(v)
            adjs[v].add(u)
        
        # Find Bob's path to root
        bob_path = [-1] * n
        bob_time = {}
        def dfs_bob(node, parent, time):
            if node == 0:
                bob_path[node] = parent
                bob_time[node] = time
                return True
            for child in adjs[node]:
                if child != parent and dfs_bob(child, node, time + 1):
                    bob_path[node] = parent
                    bob_time[node] = time
                    return True
            return False
        dfs_bob(bob, -1, 0)
        
        # DFS for Alice
        def dfs_alice(node, parent, time, income):
            # Process current node
            if time < bob_time.get(node, float('inf')):
                income += amount[node]
            elif time == bob_time.get(node, float('inf')):
                income += amount[node] // 2
            
            # If leaf node, return income
            if len(adjs[node]) == 1 and node != 0:
                return income
            
            # Continue DFS
            max_income = float('-inf')
            for child in adjs[node]:
                if child != parent:
                    child_income = dfs_alice(child, node, time + 1, income)
                    max_income = max(max_income, child_income)
            
            return max_income if max_income != float('-inf') else income
        
        return dfs_alice(0, -1, 0, 0)
