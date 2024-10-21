#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sizeofChunk = 1
        while sizeofChunk <= len(s) // 2:
            isAllEqualToThatChunk = True
            idx = 0
            chunk = s[idx:sizeofChunk+idx]
            while idx < len(s):
                isAllEqualToThatChunk = isAllEqualToThatChunk and chunk == s[idx:min(sizeofChunk+idx, len(s))]
                if not isAllEqualToThatChunk:break
                idx += sizeofChunk
            
            sizeofChunk += 1

            
            if isAllEqualToThatChunk:return isAllEqualToThatChunk
        return False
# @lc code=end

s = "aabaaba"
sss = Solution()
print(sss.repeatedSubstringPattern(s))
s = "aba"
print(sss.repeatedSubstringPattern(s))
s = "abcabcabcabc"
print(sss.repeatedSubstringPattern(s))
