from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph with both directions: (adjacency list)
        adjs = {i: [] for i in range(n)}
        for u, v in connections:
            adjs[u].append((v, 1))  # (neighbor, 1) means an original edge that needs reversing
            adjs[v].append((u, 0))  # (neighbor, 0) means this edge does not need reversing
        
        visited = set()
            
        def dfs(current_city: int) -> int:
            # Mark the current city as visited
            visited.add(current_city)
            
            # Initialize the count of reversals needed for this city
            reversal_count = 0
            
            # Explore all neighboring cities
            for neighbor_city, needs_reversing in adjs[current_city]:
                # If the neighboring city has not been visited yet
                if neighbor_city not in visited:
                    # If this road needs reversing, add 1 to the reversal count
                    reversal_count += needs_reversing
                    
                    # Recursively explore the neighbor city and add its reversal count
                    reversal_count += dfs(neighbor_city)
            
            # Return the total reversal count for this city and its neighbors
            return reversal_count

        
        # Start DFS from city 0
        return dfs(0)

# Test cases
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s = Solution()
print(s.minReorder(n, connections))  # Output: 3

n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]
print(s.minReorder(n, connections))  # Output: 2

n = 3
connections = [[1,0],[2,0]]
print(s.minReorder(n, connections))  # Output: 0

n = 3
connections = [[1,2],[2,0]]
print(s.minReorder(n, connections))  # Output: 1
