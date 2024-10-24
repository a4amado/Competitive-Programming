#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
from typing import Dict, List

from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = defaultdict(set)
        map_word = defaultdict(set)

        words = s.split(" ")
        if len(pattern) != len(words): return False
        
        for idx in range(len(pattern)):
            map[pattern[idx]].add(words[idx])
            map_word[words[idx]].add(pattern[idx])

        for _, words in map.items():
            if len(words) != 1: return False

        for _, words in map_word.items():
            if len(words) != 1: return False

        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
# @lc code=end

