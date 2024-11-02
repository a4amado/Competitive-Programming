#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        str_1 = len(word1)
        str_2 = len(word2)

        # dp = [[0 for _ in range(str_2)] for _ in range(str_1)]

        memo = {}

        def recursion(idx: int, jdx: int):
            key = (idx, jdx)
            if key in memo:return memo[key]

            if idx == str_1:
                return str_2 - jdx
            if jdx == str_2:
                return str_1 - idx

            if word1[idx] == word2[jdx]:
                memo[key] = recursion(idx + 1, jdx + 1)
            else:
                
                memo[key] = min(
                    recursion(idx + 1, jdx),
                    recursion(idx, jdx  + 1),
                )  + 1

            return memo[key]
        return recursion(0,0)

# @lc code=end


word1 = "sea"
word2 = "eat"

sol = Solution()
print(sol.minDistance(word1, word2))
