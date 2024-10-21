from typing import *
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, graph: List[List[int]]) -> List[List[int]]:
        adjs = defaultdict(list)
        for u, v in graph:
            adjs[u].append(v)
            adjs[v].append(u)
        citical =  []

        discovery = defaultdict(int)
        lowest = defaultdict(int)
        parents = defaultdict(int)
        time = 0

        def dfs(idx:int, discovery:Dict[int, int], lowest:Dict[int, int], parents:Dict[int, int]):
            nonlocal time
            lowest[idx] = discovery[idx] = time
            time += 1

            for nei in adjs[idx]:
                if nei == idx: continue
                # if not visited
                if nei not in discovery:

                    parents[nei] = idx
                    dfs(nei, discovery, lowest, parents)

                    
                    lowest[idx] = min(lowest[idx], lowest[nei])
                    
                    if lowest[nei] > discovery[idx]:
                        citical.append([idx, nei])

                # if visted but we cam from a different path
                elif nei != parents[idx]:
                    lowest[idx] = min(lowest[idx], discovery[nei])
        for i in range(n):
            if i not in discovery:
                dfs(i, discovery, lowest, parents)

        return citical