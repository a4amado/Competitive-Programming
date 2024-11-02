from typing import List

def frogJump(steps: int, heights: List[int]) -> int:
    n = len(heights)
    memo = {}

    def recur(idx: int) -> int:
        if idx in memo:
            return memo[idx]
        if idx == n - 1:
            return 0
        
        min_cost = float('inf')

        # Calculate the cost for each possible jump
        for i in range(idx + 1, min(idx +3, n)):
            cost = abs(heights[idx] - heights[i])  +  recur(i)
            min_cost = min(min_cost, cost)


        memo[idx] = min_cost
        return memo[idx]

    return recur(0)

# Example usage
print(frogJump(4, [10, 20, 30, 10]))  # Should output the correct cost
