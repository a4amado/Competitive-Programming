#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
from typing import Dict, List


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterns: Dict[str, List[int]] = {}
        ss = s.split(" ")

        if len(ss) != len(pattern):
            return False
        for i, c in enumerate(pattern):
            if patterns.get(str(c)):
                patterns[str(c)].append(i)
            else:
                patterns[str(c)] = [i]
        
        already_used_words = set()
        for i, item in enumerate(patterns):
            l= patterns.get(item, [])
            ll = [ss[x] for x in l]
            # is all strings the same
            
            
            # [start] all words in  patterns are the same
            a = {}
            for i in ll:
                a[i] = True
            if len(a) > 1:
                return False
            # [end] all words in  patterns are the same


            # [start] this words hs be already used bt other pattern
            if ll[0] in already_used_words:
                return False
            already_used_words.add(ll[0])
            # [end] this words hs be already used bt other pattern
        return True

# s = Solution()
# print(s.wordPattern("abba", "dog cat cat dog"))
# @lc code=end
l
