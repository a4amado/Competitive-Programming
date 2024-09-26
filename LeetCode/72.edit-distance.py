#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def backtrack(word1_pos: int, word2_pos: int) -> int:
            if (word1_pos, word2_pos) in memo:
                return memo[(word1_pos, word2_pos)]
            
            if word1_pos == len(word1):
                return len(word2) - word2_pos
            
            if word2_pos == len(word2):
                return len(word1) - word1_pos
            
            if word1[word1_pos] == word2[word2_pos]:
                result = backtrack(word1_pos + 1, word2_pos + 1)
            else:
                delete = 1 + backtrack(word1_pos + 1, word2_pos)
                insert = 1 + backtrack(word1_pos, word2_pos + 1)
                replace = 1 + backtrack(word1_pos + 1, word2_pos + 1)
                result = min(delete, insert, replace)
            
            memo[(word1_pos, word2_pos)] = result
            return result
        
        return backtrack(0, 0)
s = Solution()
print(s.minDistance("horse", "ros"))