import heapq
from typing import List

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # If start is equal to end, no operation is needed
        if start == end:
            return 0
        
 
        # BFS queue to explore each state
        q = [[0, start]]
        visited = set()
        visited.add((0, start))
        MOD = 100000  # We can use modulo to prevent overflow since we don't need large values
        while q:
            count, productOfTilNow = heapq.heappop(q)
            
            # Try multiplying with every number in arr
            for num in arr:
                newProduct = (productOfTilNow * num) % MOD
                
                # If we reached the target, return the steps
                if newProduct == end:
                    return count + 1
                
                if newProduct > end:
                    continue
                
                if (newProduct) in visited:continue

                visited.add((newProduct))
                heapq.heappush(q, [count+1, newProduct])
        
        # If we exhaust all options and don't find the end, return -1 (impossible)
        return -1

# Example usage:
arr = [2, 5, 7]
start = 3
end = 30
s = Solution()
print(s.minimumMultiplications(arr, start, end))


import heapq
from typing import List

class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0

        MOD = 100000
        visited = set()
        q = [(0, start)]
        
        while q:
            count, product = heapq.heappop(q)
            
            if product == end:
                return count
            
            for num in arr:
                new_product = (product * num) % MOD
                
                if new_product not in visited:
                    visited.add(new_product)
                    heapq.heappush(q, (count + 1, new_product))
        
        return -1
    
    