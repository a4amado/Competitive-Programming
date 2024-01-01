#
# @lc app=leetcode id=1455 lang=python
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#

# @lc code=start
class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        # soultion one
        # l = sentence.split(" ")
        # res =  -1
        # for idx, word in enumerate(l):
        #     if len(word) < len(searchWord):
        #         continue
        #     elif len(word) == searchWord:
        #         if word == searchWord:
        #             res = idx + 1
        #             break
        #     else:
        #         ending = len(searchWord)
        #         sub_str = word[0:ending]
        #         if sub_str == searchWord:
        #             res = idx + 1
        #             break
        # return res

        # soultion two
        # better one
        l = sentence.split(" ")
        for idx, word in enumerate(l):
            if word.startswith(searchWord):
                return idx + 1
        return -1

# @lc code=end
