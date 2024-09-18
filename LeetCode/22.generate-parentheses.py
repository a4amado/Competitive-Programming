#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from typing import List

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def backtracking(curr: str, numberOfOpenings: int, numberOfClosing: int):
            if len(curr) / 2  == n:
                if  numberOfOpenings == numberOfClosing:
                    final.append(curr[:])
                return
            if numberOfOpenings < n:
                backtracking(curr + "(", numberOfOpenings + 1, numberOfClosing)
            if numberOfClosing < numberOfOpenings:
                backtracking(curr + ")", numberOfOpenings, numberOfClosing + 1)
        backtracking("", 0, 0)
        return final
# @lc code=end
s = Solution()
s.generateParenthesis(3)