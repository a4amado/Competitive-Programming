from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adjs = {idx: set() for idx in range(n)}
        
        # Build the adjacency list (directed graph)
        for u, v in richer:
            adjs[v].add(u)
        
        # Initialize the result array with -1 (unprocessed nodes)
        mm = [-1] * n

        # DFS function to find the quietest person in the current person's subtree
        def dfs(idx: int):
            if mm[idx] != -1:  # If already computed, return the result
                return quiet[mm[idx]], mm[idx]

            # Start by assuming the current person is the quietest
            mm[idx] = idx
            minQuiet = quiet[idx]

            # Visit all neighbors (richer people)
            for nei in adjs[idx]:
                quietVal, quietIdx = dfs(nei)
                if quietVal < minQuiet:  # Update if a quieter person is found
                    minQuiet = quietVal
                    mm[idx] = quietIdx
            
            return minQuiet, mm[idx]

        # Perform DFS for each person
        for i in range(n):
            dfs(i)
        
        return mm
