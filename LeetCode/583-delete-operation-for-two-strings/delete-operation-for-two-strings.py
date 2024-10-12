
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        dp = [
            [
                0 for i in range(len(s1) + 1)
            ] for i in range(len(s2)  + 1)
        ]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[j -1] == s2[i-1]:
                    dp[i][j] =  dp[i-1][j-1] + 1
                else:
                    dp[i][j] =  max(dp[i-1][j], dp[i][j-1])
        return (len(s1) + len(s2)) -  2  * dp[-1][-1]
