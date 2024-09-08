#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = {}
        temp_letters = {}
        l,r = 0, 0
        while r < len(s) and l < len(s) :
            letter =s[r]
            if letter in temp_letters:
                sub_string[len(s[l:r])] = s[l:r]
                l, r, = temp_letters[letter]
                temp_letters = {}
            else:
                r += 1
                temp_letters[letter] = r
        sub_string[len(s[l:r])] = s[l:r]

        return  sorted(list(sub_string))[-1]
    


# @lc code=end