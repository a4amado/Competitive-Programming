class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for idx in range(len(haystack) - len(needle)  +1):
            sub_string = haystack[idx:idx+len(needle)]
            if needle == sub_string:return idx
        return -1
