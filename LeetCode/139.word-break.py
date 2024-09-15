from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        words = ""
        
        def dp(i: int) -> bool:
            nonlocal words
            if words == s:
                return True
            if i >= len(s):
                return False
            if i in visited:
                return False
            for word in wordDict:
                remainingSpace = len(s) - i
                if remainingSpace < len(word):
                    continue
                nextPartOfTheStringToCompare = s[i:i+len(word)]
                if word == nextPartOfTheStringToCompare:
                    words += nextPartOfTheStringToCompare
                    if dp(i+len(nextPartOfTheStringToCompare)):
                        return True
                    else:
                        words = words[:-len(nextPartOfTheStringToCompare)]
            visited.add(i)
            return False
        
        return dp(0)

# Test the solution
s = Solution()
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
