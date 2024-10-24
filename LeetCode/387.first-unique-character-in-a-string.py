#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

from typing import *
from collections import Counter


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)

        for idx, char in enumerate(s):
            if char == 1:return idx
        return -1

# @lc code=end

