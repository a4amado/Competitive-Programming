#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        idxs = defaultdict(list)
        for idx, char in enumerate(s):
            idxs[char].append(idx)
        max_range = float('-inf')

        for row in idxs.values():
            minVal = min(row)
            maxVal = max(row)
            max_range = max(max_range, abs(minVal - maxVal) -1)

        return -1 if max_range == float('-inf') else max_range
# @lc code=end

s = "abca"
sol = Solution()
print(sol.maxLengthBetweenEqualCharacters(s))
s = "aa"
print(sol.maxLengthBetweenEqualCharacters(s))
s = "cbzxy"
print(sol.maxLengthBetweenEqualCharacters(s))
