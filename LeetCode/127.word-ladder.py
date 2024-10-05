#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

from typing import *
from collections import deque

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList2 = {item: idx for idx, item in enumerate(wordList)}
        chars = [set() for _ in range(len(wordList[0]))] 
        for i in range(len(wordList[0])):
            for j in range(len(wordList)):
                chars[i].add(wordList[j][i])
        q = deque([])
        q.append((beginWord, 1))
        while q:
            (word, level) = q.popleft()
            if word == endWord: return level

            l = list(word)
            for i in range(len(word)):
                for j in chars[i]:
                    temp = l[i]
                    l[i] = j
                    newWord = "".join(l)
                    if newWord in wordList2:
                        q.append((newWord, level + 1))
                        del wordList2[newWord]
                    l[i] = temp
        return 0
        

# @lc code=end


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


s = Solution()
print(
    s.ladderLength(beginWord, endWord, wordList)
)


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(
    s.ladderLength(beginWord, endWord, wordList)
)

