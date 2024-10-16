class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def d(i: int, j: int) -> int:
            key = (i, j)
            if key in memo: return memo[key]

            # Base cases
            if i == len(s1):
                memo[key] =  sum(ord(c) for c in s2[j:])
                return memo[key]
            if j == len(s2):
                memo[key] =  sum(ord(c) for c in s1[i:])
                return memo[key]
            
            
            # If characters match, no deletion needed
            if s1[i] == s2[j]:
                return d(i + 1, j + 1)
            
            # Otherwise, try deleting from either string and choose the minimum
            memo[key] = min(
                ord(s1[i]) + d(i + 1, j),
                ord(s2[j]) + d(i, j + 1)
            )
            return memo[key]
        
        # return dp(0, 0)
        rows = len(s1) + 1
        cols = len(s2)  + 1

        dp = [
            ([0] * cols) for _ in range(rows)
        ]

        for j in range(1, rows):
            dp[j][0] = dp[j-1][0] + ord(s1[j-1])
        for i in range(1, cols):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
        


        for row in range(1, rows):
            for col in range(1, cols):
                if s1[row-1] == s2[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                    dp[row][col] = min(
                                    ord(s2[col-1]) + dp[row][col-1],
                                    ord(s1[row-1]) + dp[row-1][col]
                                )
                    
                
        return dp[-1][-1]