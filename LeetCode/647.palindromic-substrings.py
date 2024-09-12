#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start

class Solution:
    def countSubstrings(self, s: str) -> int:
        m = set()
        def counterFn(start: int, end: int):
            if start < 0 or end >= len(s):
                return
            
            if s[start] != s[end]:
                return
            

            while s[start] == s[end]:
                key = f"{start}.{end}"
                if key in m:
                    return

                m.add(key)

                start -= 1
                end += 1
                if start < 0 or end >= len(s):
                    return

                



        for i in range(len(s)):
            counterFn(i, i)
            counterFn(i, i+1)

        return len(m)


# @lc code=end

s = Solution()
s.countSubstrings("aaa")