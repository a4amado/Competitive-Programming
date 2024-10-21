from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length
        words.sort(key=len)
        
        # Dictionary to store the longest chain ending at each word
        dp = {word:1 for word in words}

        for word in words:
            # Try removing one character at a time
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                
                # If the predecessor exists, update the chain length
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            
        
        return max(dp.values())

# @lc code=end
words = ["a","b","ba","bca","bda","bdca"]
s = Solution()
print(s.longestStrChain(words))

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
print(s.longestStrChain(words))


