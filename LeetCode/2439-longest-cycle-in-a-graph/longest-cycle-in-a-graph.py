from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        in_current_path = [False] * n
        max_cycle = -1

        def dfs(node: int, depth: int) -> None:
            nonlocal max_cycle
            if node == -1:
                return
            if in_current_path[node]:
                max_cycle = max(max_cycle, depth - depths[node])
                return
            if visited[node]:
                return

            visited[node] = True
            in_current_path[node] = True
            depths[node] = depth

            next_node = edges[node]
            dfs(next_node, depth + 1)

            in_current_path[node] = False

        depths = {}
        for i in range(n):
            if not visited[i]:
                dfs(i, 0)

        return max_cycle

