class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(idx: int) -> int:
            if idx in memo:
                return 0  # We've already counted this path, so return 0 to avoid double counting

            if idx == len(s):
                return 1  # Valid path reached the end

            if s[idx] == "0":
                return 0  # Invalid encoding

            count = 0

            # Single digit decode
            count += dfs(idx + 1)

            # Two digit decode
            if idx + 1 < len(s):
                two_digit = int(s[idx:idx+2])
                if 10 <= two_digit <= 26:
                    count += dfs(idx + 2)

            memo[idx] = count  # Memoize the result
            return count

        return dfs(0)

s = Solution()
print(s.numDecodings("226"))