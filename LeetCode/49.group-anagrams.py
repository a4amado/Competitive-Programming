#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from typing import List, Dict

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the letter of the words
        # make a dict { 'unique word': [list of words] }
        mm: Dict[str, List[str]] = {}
        for idx, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word not in mm:
                mm[sorted_word] = [word]
            else:
                mm[sorted_word].append(word)
        return list(mm.values())
# @lc code=end

