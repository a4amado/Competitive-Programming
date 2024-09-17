from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remaining: int, combination: List[int]):
            if remaining == 0:
                # Sort the combination to ensure consistent ordering
                sorted_combination = sorted(combination)
                # Convert to tuple for hashability
                combination_tuple = tuple(sorted_combination)
                if combination_tuple not in seen:
                    result.append(sorted_combination)
                    seen.add(combination_tuple)
                return
            if remaining < 0:
                return
            
            for i in candidates:
                if i <= remaining:
                    combination.append(i)
                    # Pass i instead of i+1 to allow reuse of the same number
                    dfs(remaining - i, combination)
                    combination.pop()

        result = []
        seen = set()  # To keep track of unique combinations
        candidates.sort()  # Sort candidates to optimize
        dfs(target, [])
        return result

# Test the solution
s = Solution()
print(s.combinationSum([2,3,7], 7))