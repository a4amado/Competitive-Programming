class Solution:
    def editDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def backtrack(idx1: int, idx2: int) -> int:
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if idx1 == len(word1):
                return len(word2) - idx2

            if idx2 == len(word2):
                return len(word1) - idx1

            if word1[idx1] == word2[idx2]:
                result = backtrack(idx1 + 1, idx2 + 1)
            else:
                delete = 1 + backtrack(idx1 + 1, idx2)
                insert = 1 + backtrack(idx1, idx2 + 1)
                replace = 1 + backtrack(idx1 + 1, idx2 + 1)
                result = min(delete, insert, replace)

            memo[(idx1, idx2)] = result
            return result

        # return backtrack(0, 0)
        dp = [
            [
                0  for  i in range(len(word1) + 1)
            ] for  i in range(len(word2) + 1)
        ]
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j

        for idx1 in range(1, len(dp)):
            for idx2 in range(1, len(dp[0])):
                if word1[idx2 -1] == word2[idx1 -1]:
                    dp[idx1][idx2] = dp[idx1 -1][idx2-1]
                else:
                    dp[idx1][idx2] = 1 + min(
                         dp[idx1][idx2-1],
                         dp[idx1 -1][idx2],
                         dp[idx1-1][idx2-1]
                    )
        for i in dp:
            print(i)
        return dp[-1][-1]  # Corrected return statement

str1 = "geek"
str2 = "gesek"

s = Solution()
print(
    s.editDistance(str1, str2)
)

str1 = "gfg"
str2 = "gfg"
print(
    s.editDistance(str1, str2)
)

str1 = "ecfbefdcfca"
str2 = "badfcbebbf"

print(
    s.editDistance(str1, str2)
)