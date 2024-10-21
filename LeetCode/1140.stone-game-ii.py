
from functools import cache
from itertools import accumulate
from typing import *

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def dfs(i, m):
            if m * 2 >= n - i:
                return s[n] - s[i]
            return max(
                s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m << 1 | 1)
            )

        n = len(piles)
        s = list(accumulate(piles, initial=0))
        return dfs(0, 1)

# Test cases
piles = [2, 7, 9, 4, 4]
print(list(accumulate(piles, initial=0)))

# print(Solution().stoneGameII(piles))  # Should return 10

# piles = [1, 2, 3, 4, 5, 100]
# print(Solution().stoneGameII(piles))  # Should return 104
