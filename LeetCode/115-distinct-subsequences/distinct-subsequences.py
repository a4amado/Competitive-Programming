class Solution:
    def numDistinct(self, str1: str, sub: str) -> int:
        s = ""
        chars = {i:True for i in sub}
        for i in str1:
            if i in chars:
                s += i
        memo = {}
        def b(idx: int, jdx: int, l: int):
            if l == len(sub): return 1
            
            if idx == len(s) or jdx == len(sub):return 0
            key = (idx, jdx, l)

            if key in memo: return memo[key]
            c = 0
            if s[idx] == sub[jdx]:
                c += b(idx+1, jdx+1, l + 1)
            c += b(idx+1, jdx, l)
            
            memo[key] = c
            return memo[key]
        # return b(0, 0, 0)
        dp = [
            [
                0 if j != 0 else 1 for i in range(len(s) + 1)
            ]  for j in range(len(sub) + 1)
        ]
        
        for idx in range(1, len(dp)):
            for jdx in range(1, len(dp[0])):
                if sub[idx -1] == s[jdx-1]:
                    dp[idx][jdx] = dp[idx-1][jdx-1]
                dp[idx][jdx] += dp[idx][jdx-1]
                    

        return dp[-1][-1]
            