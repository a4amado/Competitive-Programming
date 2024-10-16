class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        wildcard = "*"
        singular = "?"

        # dp table, initialize all as False initially
        dp = [[False] * (len(text) + 1) for _ in range(len(pattern) + 1)]

        # Base case: empty pattern and empty text is a match
        dp[0][0] = True

        # Base case: when text is empty but pattern is not, check for wildcard '*'
        for idx in range(1, len(pattern) + 1):
            if pattern[idx - 1] == wildcard:
                dp[idx][0] = dp[idx - 1][0]  # '*' can match empty text
        

        # Fill the DP table from top-left to bottom-right
        for idx in range(1, len(pattern) + 1):
            for jdx in range(1, len(text) + 1):
                currpattern = pattern[idx - 1]
                currChar = text[jdx - 1]

                dp[idx][jdx] = dp[idx - 1][jdx] or dp[idx][jdx - 1]


                if currpattern == singular:
                    dp[idx][jdx] = dp[idx - 1][jdx - 1]
                elif currpattern == wildcard:
                    dp[idx][jdx] = dp[idx - 1][jdx] or dp[idx][jdx - 1]
                else:
                    dp[idx][jdx] = currpattern == currChar and dp[idx - 1][jdx - 1]

        # The result will be stored in dp[len(pattern)][len(text)], meaning the entire pattern matches the entire text
        return dp[len(pattern)][len(text)]
          


# s = "cb"
# p = "?a"
# ss = Solution()
# print(ss.isMatch(s, p))
# s = "aa"
# p = "*"
# print(ss.isMatch(s, p))

# s = "adceb"
# p = "*a*b"
# print(ss.isMatch(s, p))



s = "cb"
p = "?a"
ss = Solution()
print(ss.isMatch(s, p))
s = "aa"
p = "*"
print(ss.isMatch(s, p))

s = "adceb"
p = "*a*b"
print(ss.isMatch(s, p))
