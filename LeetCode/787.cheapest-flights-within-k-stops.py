
from typing import List

import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))

        # Priority queue for BFS-like exploration with (cost, current node, stops left)
        heap = [(0, src, k + 1)]  # (current price, current city, stops remaining)
        visited = {}

        while heap:
            price, node, stops = heapq.heappop(heap)

            # If we reach the destination, return the cost
            if node == dst:
                return price

            # If we still have stops left, explore the next cities
            if stops > 0:
                for neighbor, cost in graph[node]:
                    new_price = price + cost
                    if (neighbor, stops - 1) not in visited or visited[(neighbor, stops - 1)] > new_price:
                        visited[(neighbor, stops - 1)] = new_price
                        heapq.heappush(heap, (new_price, neighbor, stops - 1))

        return -1  # If no route is found within K stops
