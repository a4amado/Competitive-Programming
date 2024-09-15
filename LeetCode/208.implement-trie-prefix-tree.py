
#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

class TreeNode():
    def __init__(self) -> None:
        self.val = {}
        self.word_end = False

class Trie:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.val:
                newNode = TreeNode()
                curr.val[char] = newNode
            curr = curr.val[char]
        curr.word_end = True


    def search(self, word: str) -> bool:
        curr = self.head
        if not curr:
            return False
        for char in word:
            if char not in curr.val:
                return False
            curr = curr.val[char]
        return curr.word_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        if not curr:
            return False
        for char in prefix:
            if char not in curr.val:
                return False
            curr = curr.val[char]
        return True


# Your Trie object will be instantiated and called as such:
word = "sadasd"
prefix = "sad"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2, param_3)
# @lc code=end

