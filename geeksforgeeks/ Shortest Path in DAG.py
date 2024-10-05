from  typing import *
from collections import deque


def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    adjs = [[] for _ in range(n)]
    distances = [float('inf') for _ in range(n)] 
    for edge in edges:
        [src, dest, weight] = edge
        adjs[src].append([dest, weight])

    def dfs(idx:int, sumTilNow: int):
        if distances[idx] > sumTilNow:
            distances[idx] = sumTilNow
        else: return

        for nei in adjs[idx]:
            [dest, weight] = nei
            dfs(dest, sumTilNow + weight)
    
    dfs(0, 0)
    for i in range(len(distances)):
        if distances[i] == float('inf'):
            distances[i] = -1
    return distances

print(
    shortestPathInDAG(
        4,6,
[[0,1,360],
[0,3,242],
[1,2,317],
[0,2,306]]
    )
)



# print(
#     shortestPathInDAG(0,0, [[2,0,4],[0,1,3],[2,1,2]])
# )
# print(
#     shortestPathInDAG(0,0, [[2,1,5],
# [0,2,3],
# [0,1,2],
# [2,3,1]])
# )

# [[2,0,4],[0,1,3],[2,1,2]]
