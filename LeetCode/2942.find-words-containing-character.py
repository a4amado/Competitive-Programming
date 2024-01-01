#
# @lc app=leetcode id=2942 lang=python
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        lisst = []
        for idx, item in enumerate(words):
            if x in item:
                lisst.append(idx)
        return lisst
# @lc code=end

