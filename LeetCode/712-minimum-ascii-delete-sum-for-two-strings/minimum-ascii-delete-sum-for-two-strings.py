class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def dp(i: int, j: int) -> int:
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
                return dp(i + 1, j + 1)
            
            # Otherwise, try deleting from either string and choose the minimum
            memo[key] = min(
                ord(s1[i]) + dp(i + 1, j),
                ord(s2[j]) + dp(i, j + 1)
            )
            return memo[key]
        return dp(0, 0)