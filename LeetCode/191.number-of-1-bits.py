#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
from collections import Counter

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.memo = {}
    def hammingWeight(self, n: int) -> int:
        key = str(n)
        c = Counter(list(str(key)))
        self.memo[key] = c["1"]
        return self.memo[key]
s= Solution()
print(s.hammingWeight("01111111111111111111111111111101"))
# @lc code=end

