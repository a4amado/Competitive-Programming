#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


from typing import Optional

# @lc code=start

class TrieNode:
    def __init__(self):
        self.child = {}  # Using a dictionary instead of a fixed-size array
        self.word_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.word_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idxOfChar: int):
            if idxOfChar == len(word):
                return node.word_end

            c = word[idxOfChar]
            if c == ".":
                for child in node.child:
                    if dfs(node.child[child], idxOfChar + 1):
                        return True
                return False
            else:
                if c not in node.child:
                    return False
                return dfs(node.child[word[idxOfChar]], idxOfChar + 1)

        return dfs(self.root, 0)
# @lc code=end

wordDictionary =  WordDictionary()
wordDictionary.addWord("bad")
print(wordDictionary.search("bad"))


  


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

