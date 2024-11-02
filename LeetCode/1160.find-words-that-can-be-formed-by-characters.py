#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        sumLength = 0
        for word in words:
            is_good = True
            count = Counter(word)
            for char, count in count.items():
                if count > chars[char]:
                    is_good = False
                    break
            if is_good:
                sumLength += len(word)
        return sumLength
# @lc code=end


words = ["cat","bt","hat","tree"]
chars = "atach"

sol = Solution()

sol.countCharacters(words, chars)