#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return ""
        mapedDigets = {
            2:"abc",
            3:"def",
            4:"ghi",
            5: "jkl",
            6: "mno",
            7:"pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []
        def dfs(idx: int, curr: str):
            if idx == len(digits):
                res.append(curr)
                return
            
            for digit in mapedDigets[int(digits[idx])]:
                dfs(idx + 1, curr + digit)
        dfs(0, "")
        return res


# @lc code=end

s = Solution()
print(s.letterCombinations(""))
