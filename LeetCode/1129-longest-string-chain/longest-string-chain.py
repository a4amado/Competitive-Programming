from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length
        words.sort(key=len)
        
        # Dictionary to store the longest chain ending at each word
        dp = {}
        
        max_chain = 0
        
        for word in words:
            # Initialize the chain length for the current word
            dp[word] = 1
            
            # Try removing one character at a time
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                
                # If the predecessor exists, update the chain length
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            
            # Update the maximum chain length
            max_chain = max(max_chain, dp[word])
        
        return max_chain