from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        q = []
        visited = {}
        heapq.heappush(q, (0, -1, src))
        while q:
            weight, count, node = heapq.heappop(q)
            if count > k:
                continue
            if node == dst:
                return weight
            if node in visited and visited[node] <= count:
                continue
            visited[node] = count

            for v, w in graph[node]:
                heapq.heappush(q, (weight + w, count + 1, v))
        return -1

# Test cases
test_cases = [
    (3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1),
    (4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
]

s = Solution()
for i, (n, flights, src, dst, k) in enumerate(test_cases, 1):
    result = s.findCheapestPrice(n, flights, src, dst, k)
    print(f"Test case {i}: {result}")